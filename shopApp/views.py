from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    my_context = {
        'user' : 'Carlos',
        'message' : 'Largo de aquí!',
        'special_offers' : [
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