from django.test import TestCase,Client
from django.urls import reverse
from .models import MainWebs,DetailsWeb
from django.contrib.auth.models import User


class TestWebscrapper(TestCase):

    def setUp(self):
        self.URL = "http://www.google.com"

    def test_db_from_form(self):
        #posting url from form
        client = Client()
        response = client.post(reverse("home_inicio"),{"url_a_buscar":self.URL})

        #retrieve objects from database
        q = MainWebs.objects.all().first()
        self.assertEqual(q.url, self.URL)
        #Basicamente, si funciona este test, funciona todo el proceso.


    
