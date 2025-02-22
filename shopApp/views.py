from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    my_context = {
        'message' : 'Largo de aquí!',
        'products' : [
            'Mascarilla hidratante de sábila.',
            'Consola de videojuegos portátil XE150',
            'Reloj de pulsera Gótico de Snoopy',
            'Camisa para caballero de algodón',
            'Peluche de Batman tamaño real',
        ],
    }
    return render(request, 'shopApp/index.html', context=my_context)
    #return HttpResponse("Hola mundo desde Django!")