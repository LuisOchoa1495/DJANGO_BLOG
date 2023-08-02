from datetime import datetime, timedelta
from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify
from django.urls import reverse_lazy
#apps de teceros
from model_utils.models import TimeStampedModel
from ckeditor_uploader.fields import RichTextUploadingField

# managers
from .managers import EntryManager

# Create your models here.
class Category(TimeStampedModel):
    """Categorias de entrada"""
    short_name = models.CharField(
        'Nombre corto',
        max_length=15,
        unique=True,
        )
    name=models.CharField(
        'Nombre',
        max_length=30
        )
        
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categoria'

    def __str__(self):
        return self.name
    

class Tag(TimeStampedModel):
    name=models.CharField(
        'Nombre',
        max_length=30
    )
    class Meta:
        verbose_name = 'Etiqueta'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.name

class Entry(TimeStampedModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    category=models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    tag=models.ManyToManyField(Tag)
    title=models.CharField(
        'Titulo',
        max_length=200
    )
    resume=models.TextField('Resumen')
    content= RichTextUploadingField('contenido')
    public=models.BooleanField(default=False)
    image=models.ImageField(
        'Imagen',
        upload_to='Entry',
    )
    portada=models.BooleanField(default=False)
    in_home=models.BooleanField(default=False)
    #urls con slug -posicionamiento 
    slug=models.SlugField(editable=False,max_length=300)

    objects=EntryManager()

    class Meta:
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse_lazy(
            'entrada_app:entry-detail',
            kwargs={
                'slug' : self.slug
            }
        )    
    
    
    def save(self,*args,**kwargs):
        #claculamos la hora
        now=datetime.now()
        total_time=timedelta(
            hours=now.hour,
            minutes=now.minute,
            seconds=now.second
        )
        seconds= int(total_time.total_seconds())
        slug_unique='%s %s' % (self.title, str(seconds)) 
        self.slug = slugify(slug_unique)

        super(Entry, self).save(*args,**kwargs)

