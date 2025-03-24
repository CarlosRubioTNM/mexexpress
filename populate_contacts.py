#Cargar los elementos necesarios para utilizar los modulos de django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mexexpress.settings')
import django
django.setup()

#Script para poblar la tabla Product
from faker import Faker
import random
from shopApp.models import Contact

fake_generator = Faker()

def populate_contact(n_products=5):
    for i in range(n_products):
        fake_full_name = fake_generator.name()
        fake_address = fake_generator.address()
        fake_phone = fake_generator.phone_number()
        fake_email = fake_generator.email()
        fake_is_active = random.random() > 0.5

        contact = Contact.objects.get_or_create(
            contact_full_name = fake_full_name,
            contact_address = fake_address,
            contact_phone = fake_phone,
            contact_email = fake_email,
            contact_is_active = fake_is_active
        )

if __name__ == '__main__':
    print('Empezar a poblar la base de datos.')
    populate_contact(30)
    print('Finalizado.')