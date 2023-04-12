from django.test import TestCase,Client
from django.urls import reverse
from .models import MainWebs,DetailsWeb
from django.contrib.auth.models import User


class TestWebscrapper(TestCase):

    def setUp(self):
        self.URL = "http://www.google.com"
        User.objects.create_user(username="test123@test123.cl",password="test123")
        User.objects.create_user(username="test122@test122.cl",password="test122")

    def test_login(self):
        client = Client()
        response = client.post(
            reverse("home_login"),
            {
                "email":"test123@test123.cl",
                "password":"test123"

                })
        self.assertEqual(response.url, reverse("home_inicio"))
    
    def test_db_from_form(self):
        #posting url from form
        client = Client()
        user = User.objects.get(username="test123@test123.cl")
        b = client.login(username="test123@test123.cl",password="test123")
        response = client.post(reverse("home_inicio"),{"url_a_buscar":self.URL})
        
        #retrieve objects from database
        q = MainWebs.objects.get(user=user)
        self.assertEqual(q.url, self.URL)
        #Basicamente, si funciona este test, funciona todo el proceso.


    
