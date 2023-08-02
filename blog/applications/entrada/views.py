from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView
)
from .models import Entry,Category

# Create your views here.
class EntryListView(ListView):
    template_name = "entrada/lista.html"
    context_object_name="entradas"
    paginate_by = 9

    def get_context_data(self, **kwargs):
        context = super(EntryListView, self).get_context_data(**kwargs)
        context["categorias"] = Category.objects.all()
        return context

    def get_queryset(self):
        kword=self.request.GET.get("kword", '')
        categoria=self.request.GET.get("categoria", '')
        #consulta
        resultado=Entry.objects.buscar_entrada(kword,categoria)
        return resultado
    

class EntryDetailView(DetailView):
    model = Entry
    template_name = "entrada/detail.html"

