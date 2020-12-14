from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from . import views
from .models import Kategoria
from rest_framework import status
from django.utils.http import urlencode
from django import urls


class KategoriaTests(APITestCase):

    def post_book_Kategoria(self, name):
        url = reverse(views.KategoriaList.name)
        data = {'name': name}
        response = self.client.post(url, data, format='json')
        return response
