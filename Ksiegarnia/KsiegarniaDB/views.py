from django.shortcuts import render
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, status, generics
from django.contrib.auth.models import User
from .models import Ksiazka, Adres, User, Autor, Klient, Kategoria, Paragon
from .serializers import KsiazkaSerializer, AdresSerializer, UserSerializer, AutorSerializer, KlientSerializer,\
    KategoriaSerializer, ParagonSerializer


# KSIAZKA ====================================================================================


class KsiazkaList(generics.ListCreateAPIView):
    queryset = Ksiazka.objects.all()
    serializer_class = KsiazkaSerializer
    name = 'ksiazka-list'


class KsiazkaDetail(generics.RetrieveDestroyAPIView):
    queryset = Ksiazka.objects.all()
    serializer_class = KsiazkaSerializer
    name = 'ksiazka-detail'


# ADRES ====================================================================================


class AdresList(generics.ListCreateAPIView):
    queryset = Adres.objects.all()
    serializer_class = AdresSerializer
    name = 'adres-list'


class AdresDetail(generics.RetrieveDestroyAPIView):
    queryset = Adres.objects.all()
    serializer_class = AdresSerializer
    name = 'adres-detail'


# AUTOR ====================================================================================


class AutorList(generics.ListCreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    name = 'autor-list'


class AutorDetail(generics.RetrieveDestroyAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    name = 'autor-detail'


# KLIENT ====================================================================================


class KlientList(generics.ListCreateAPIView):
    queryset = Klient.objects.all()
    serializer_class = KlientSerializer
    name = 'klient-list'


class KlientDetail(generics.RetrieveDestroyAPIView):
    queryset = Klient.objects.all()
    serializer_class = KlientSerializer
    name = 'klient-detail'


# KATEGORIA ====================================================================================


class KategoriaList(generics.ListCreateAPIView):
    queryset = Kategoria.objects.all()
    serializer_class = KategoriaSerializer
    name = 'kategoria-list'


class KategoriaDetail(generics.RetrieveDestroyAPIView):
    queryset = Kategoria.objects.all()
    serializer_class = KategoriaSerializer
    name = 'kategoria-detail'


# PARAGON ====================================================================================


class ParagonList(generics.ListCreateAPIView):
    queryset = Paragon.objects.all()
    serializer_class = ParagonSerializer
    name = 'paragon-list'


class ParagonDetail(generics.RetrieveDestroyAPIView):
    queryset = Paragon.objects.all()
    serializer_class = ParagonSerializer
    name = 'paragon-detail'


# USER ====================================================================================


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'


class UserDetail(generics.RetrieveDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({'adresy': reverse(AdresList.name, request=request),
                         'users': reverse(UserList.name, request=request),
                         'kategorie': reverse(KategoriaList.name, request=request),
                         'paragony': reverse(ParagonList.name, request=request),
                         'ksiazki': reverse(KsiazkaList.name, request=request),
                         'klienci': reverse(KlientList.name, request=request),
                         'autorzy': reverse(AutorList.name, request=request)
                         })
