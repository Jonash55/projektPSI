from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from rest_framework import status
from django.utils.html import urlencode

from . import views
from .models import Kategoria


class KategoriaTests(APITestCase):
    def post_kategoria(self, Nazwa, Opis):
        url = reverse(views.KategoriaList.name)
        data = {'Nazwa': Nazwa, 'Opis': Opis}
        response = self.client.post(url, data, format='json')
        return response

    def test_post_and_get(self):
        nowe_Nazwa = 'Science'
        nowe_Opis = 'Opis kategorii Science'
        response = self.post_kategoria(nowe_Nazwa, nowe_Opis)
        assert response.status_code == status.HTTP_201_CREATED
        assert Kategoria.objects.count() == 1
        assert Kategoria.objects.get().Nazwa == nowe_Nazwa

    def test_filter_Kategoria_nazwa(self):
        nowe_Nazwa = 'Sci-Fi'
        nowe_Nazwa_2 = 'Wiersz'
        nowe_Opis = 'Opis kategorii Sci-Fi'
        nowe_Opis_2 = 'Opis kategorii wiersz'

        self.post_kategoria(nowe_Nazwa, nowe_Opis)
        self.post_kategoria(nowe_Nazwa_2, nowe_Opis_2)
        filter_Kategoria_nazwa = {'Nazwa': nowe_Nazwa}
        url = '{0}?{1}'.format(reverse(views.KategoriaList.name), urlencode(filter_Kategoria_nazwa))
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 2
        assert response.data['results'][0]['Nazwa'] == nowe_Nazwa

    def test_post_existing_Kategoria_nazwa(self):
        nowe_Nazwa = 'Science'
        nowe_Opis = 'Opis kategorii Science'
        response = self.post_kategoria(nowe_Nazwa, nowe_Opis)
        assert response.status_code == status.HTTP_201_CREATED
        assert Kategoria.objects.count() == 1
        assert Kategoria.objects.get().Nazwa == nowe_Nazwa

    def test_get_book_category_collection(self):
        nowe_Nazwa = 'Dramat'
        nowe_Opis = 'Opis kategorii Dramat'
        self.post_kategoria(nowe_Nazwa, nowe_Opis)
        url = reverse(views.KategoriaList.name)
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1
        assert response.data['results'][0]['Nazwa'] == nowe_Nazwa
