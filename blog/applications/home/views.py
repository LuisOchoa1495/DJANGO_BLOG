import datetime
#
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse

from django.views.generic import (
    TemplateView,
    CreateView,
)
#apps entrada
from applications.entrada.models import Entry

#models
from .models import Home
#forms
from .forms import SuscribersForm,ContactForm

class HomePageView(TemplateView):
    template_name = "home/index.html"
    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        #cargamos home
        context["home"] = Home.objects.latest('-created')         
        #contexto de protada
        context["portada"] = Entry.objects.entrada_en_portada() 
        #contexto para los articulos en home
        context["entradas_home"] = Entry.objects.entradas_en_home()
        #contexto para las entradas recientes
        context["entradas_recientes"] = Entry.objects.entradas_recientes()
        #enviamos formulario de suscribsion
        context["form"] = SuscribersForm
        return context


class SuscriberCreateView(CreateView):
    form_class = SuscribersForm
    success_url='.'

class ContactCreateView(CreateView):
    form_class = ContactForm
    success_url='.'
   

