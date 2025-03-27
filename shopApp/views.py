from django.shortcuts import render
from django.http import HttpResponse
from shopApp.models import Product, Contact

# Create your views here.
def index(request):
    product_list = Product.objects.all()
    special_offers = Product.objects.filter(product_is_offer=True)
    my_context = {
        'message' : 'Largo de aquí!',
        'special_offers' : special_offers,
        'product_list' : product_list,
        'special_offers_2' : [
            {
                'name' : 'Mascarilla hidratante de sábila',
                'cost' : 14.00
            },
            {
                'name' : 'Consola de videojuegos portátil XE150',
                'cost' : 450.00
            },
            {
                'name' : 'Reloj de pulsera Gótico de Snoopy',
                'cost' : 160.00
            },
            {
                'name' : 'Camisa para caballero de algodón',
                'cost' : 200.00
            },
            {
                'name' : 'Peluche de Batman tamaño real',
                'cost' : 15600.00
            },
            {
                'name' : 'Otra cosa',
                'cost' : 120.00
            },
        ],
    }
    return render(request, 'shopApp/index.html', context=my_context)
    #return HttpResponse("Hola mundo desde Django!")

def about(request):
    contact_list = Contact.objects.filter(contact_is_active=True).order_by("contact_full_name")
    return render(request, 'shopApp/about.html', context={'contacts' : contact_list})