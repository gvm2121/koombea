from django.urls import path
from .views import *


urlpatterns = [
    path('',home_login,name="home_login"),
    path('home',home_inicio,name="home_inicio"),
    path('logout',home_logout,name="home_logout"),
    path('details/<int:id>',home_detalles,name="home_details"),
    
]
