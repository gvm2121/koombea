from django.urls import path
from .views import *


urlpatterns = [
    path('',home_inicio,name="home_inicio"),
    path('details',home_detalles,name="home_detalles"),
    
]
