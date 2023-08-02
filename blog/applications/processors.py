from applications.home.models import Home
#proceso para recuperar correo ytelewofno de home

def home_contact(request):
    home=Home.objects.latest('created')
    return {
        'phone':home.phone,
        'correo':home.contact_email,
    }