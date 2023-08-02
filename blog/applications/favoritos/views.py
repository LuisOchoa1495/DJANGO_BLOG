from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy,reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import(
    ListView,
    View,
    DeleteView,
)
from .models import Favorities
from applications.entrada.models import Entry

# Create your views here.
class UserPageView(LoginRequiredMixin, ListView):
    template_name="favoritos/perfil.html"
    context_object_name="entradas_user"
    login_url=reverse_lazy("users_app:user-login")

    def get_queryset(self):
        return Favorities.objects.entradas_user(self.request.user)
    
class AddFavoritos(View,LoginRequiredMixin):
    login_url=reverse_lazy("users_app:user-login")
    def post(self,request,*args,**kwargs):
        #recuperar usuario
        usuario=self.request.user
        entrada=Entry.objects.get(id=self.kwargs['pk'])
        #registramos favorito
        Favorities.objects.create(
            user=usuario,
            entry=entrada,
        )
        return HttpResponseRedirect(
            reverse(
                'favoritos_app:perfil'
            )
        )
    
class FavoritesDeleteView(DeleteView):
    model = Favorities
    success_url=reverse_lazy("favoritos_app:perfil")
      
        
