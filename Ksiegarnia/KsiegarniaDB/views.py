from django.shortcuts import render
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, status, generics
from django.contrib.auth.models import User
from .models import Ksiazka, Adres, User, Autor, Klient, Kategoria, Paragon
from .serializers import KsiazkaSerializer, AdresSerializer, UserSerializer, AutorSerializer, KlientSerializer,\
    KategoriaSerializer, ParagonSerializer
from django_filters import AllValuesFilter, DateTimeFilter, NumberFilter, FilterSet

# KSIAZKA ====================================================================================


class KsiazkaList(generics.ListCreateAPIView):
    queryset = Ksiazka.objects.all()
    serializer_class = KsiazkaSerializer
    name = 'ksiazka-list'
    search_fields = ['idAutora', 'idKategorii', 'tytul', 'rok_wydania', 'idKsiazki']
    ordering_fields = ['tytul', 'idAutora', 'idKategorii', 'cena_brutto', 'cena_netto', 'idKsiazki']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class KsiazkaDetail(generics.RetrieveDestroyAPIView):
    queryset = Ksiazka.objects.all()
    serializer_class = KsiazkaSerializer
    name = 'ksiazka-detail'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# ADRES ====================================================================================


class AdresList(generics.ListCreateAPIView):
    queryset = Adres.objects.all()
    serializer_class = AdresSerializer
    name = 'adres-list'
    ordering_fields = ['Miasto', 'Wojewodztwo']
    search_fields = ['Miasto', 'Wojewodztwo', 'Ulica', 'KodPocztowy']
    permission_classes = [permissions.IsAuthenticated]


class AdresDetail(generics.RetrieveDestroyAPIView):
    queryset = Adres.objects.all()
    serializer_class = AdresSerializer
    name = 'adres-detail'
    permission_classes = [permissions.IsAuthenticated]


# AUTOR ====================================================================================
class AutorFilter(FilterSet):
    from_birthdate = DateTimeFilter(field_name='DataUrodzenia', lookup_expr='gte')
    to_birthdate = DateTimeFilter(field_name='DataUrodzenia', lookup_expr='lte')

    class Meta:
        model = Autor
        fields = ['from_birthdate', 'to_birthdate']


class AutorList(generics.ListCreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    filter_class = AutorFilter
    name = 'autor-list'
    ordering_fields = ['Nazwisko', 'DataUrodzenia']
    search_fields = ['Imie', 'Nazwisko', 'idAutora', 'ksiazka__tytul']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AutorDetail(generics.RetrieveDestroyAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    name = 'autor-detail'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# KLIENT ====================================================================================


class KlientList(generics.ListCreateAPIView):
    queryset = Klient.objects.all()
    serializer_class = KlientSerializer
    name = 'klient-list'
    ordering_fields = ['Nazwisko', 'idKlienta', 'Jan', 'idAdresu', 'idUsera']
    filterset_fields = ['czyUser']
    search_fields = ['Nazwisko', 'Imie', 'idKlienta']
    permission_classes = [permissions.IsAuthenticated]


class KlientDetail(generics.RetrieveDestroyAPIView):
    queryset = Klient.objects.all()
    serializer_class = KlientSerializer
    name = 'klient-detail'
    permission_classes = [permissions.IsAuthenticated]


class UpdateImie(generics.UpdateAPIView):
    queryset = Klient.objects.all()
    serializer_class = KlientSerializer
    permission_classes = (permissions.IsAuthenticated,)

# KATEGORIA ====================================================================================


class KategoriaList(generics.ListCreateAPIView):
    queryset = Kategoria.objects.all()
    serializer_class = KategoriaSerializer
    name = 'kategoria-list'
    search_fields = ['Nazwa', 'ksiazka__tytul']
    ordering_fields = ['Nazwa', 'ksiazka', 'idKategorii']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class KategoriaDetail(generics.RetrieveDestroyAPIView):
    queryset = Kategoria.objects.all()
    serializer_class = KategoriaSerializer
    name = 'kategoria-detail'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# PARAGON ====================================================================================
class ParagonFilter(FilterSet):
    min_price = NumberFilter(field_name='suma', lookup_expr='gte')
    max_price = NumberFilter(field_name='suma', lookup_expr='lte')
    idKlienta = AllValuesFilter(field_name='idKlienta')

    class Meta:
        model = Paragon
        fields = ['min_price', 'max_price', 'idKlienta']


class ParagonList(generics.ListCreateAPIView):
    queryset = Paragon.objects.all()
    serializer_class = ParagonSerializer
    name = 'paragon-list'
    filter_class = ParagonFilter
    ordering_fields = ['idParagonu', 'idUsera', 'idKlienta', 'suma', 'dataWystawienia']
    search_fields = ['suma', 'idUsera', 'idKlienta', 'idParagonu']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ParagonDetail(generics.RetrieveDestroyAPIView):
    queryset = Paragon.objects.all()
    serializer_class = ParagonSerializer
    name = 'paragon-detail'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# USER ====================================================================================


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filterset_fields = ['status']
    ordering_fields = ['idUsera', 'username', 'Email']
    name = 'user-list'
    permission_classes = [permissions.IsAuthenticated]


class UserDetail(generics.RetrieveDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'
    permission_classes = [permissions.IsAuthenticated]


class ApiRoot(generics.GenericAPIView):
    name = 'Widok ogólny'

    def get(self, request, *args, **kwargs):
        return Response({'Użytkownicy': reverse(UserList.name, request=request),
                         'Klienci': reverse(KlientList.name, request=request),
                         'Adresy': reverse(AdresList.name, request=request),
                         'Kategorie': reverse(KategoriaList.name, request=request),
                         'Autorzy': reverse(AutorList.name, request=request),
                         'Ksiazki': reverse(KsiazkaList.name, request=request),
                         'Paragony': reverse(ParagonList.name, request=request),
                         })
