#Cargar los elementos necesarios para utilizar los modulos de django
import os
os.environ.setdefault('DJANGO_SETTING_MODULE', 'mexexpress.settings')
import django
django.setup()

#Script para poblar la tabla Product
from faker import Faker
import random
from shopApp.models import Product

fake_generator = Faker()


if __name__ == '__main__':
    print('Empezar a poblar la base de datos.')

    print('Finalizado.')