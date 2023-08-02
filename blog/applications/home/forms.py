from django import forms

#models
from .models import Suscribers,Contacto

class SuscribersForm(forms.ModelForm):
    class Meta:
        model=Suscribers
        fields=(
            'email',
        )
        widgets={
            'email': forms.EmailInput(
                attrs={
                    'placeholder':'Correo electrónico...',
                    
                }
            ),
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contacto
        fields=('__all__')