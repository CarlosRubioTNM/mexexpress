from django.urls import path
from shopApp.views import index

urlpatterns = [
    path('',index)
]