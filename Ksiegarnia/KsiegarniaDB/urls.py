from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls')),
    path('adresy/', views.AdresList.as_view(), name=views.AdresList.name),
    path('adresy/<int:pk>/', views.AdresDetail.as_view(), name=views.AdresDetail.name),
    path('ksiazka/', views.KsiazkaList.as_view(), name=views.KsiazkaList.name),
    path('ksiazka/<int:pk>/', views.KsiazkaDetail.as_view(), name=views.KsiazkaDetail.name),
    path('paragon/', views.ParagonList.as_view(), name=views.ParagonList.name),
    path('paragon/<int:pk>/', views.ParagonDetail.as_view(), name=views.ParagonDetail.name),
    path('autor/', views.AutorList.as_view(), name=views.AutorList.name),
    path('autor/<int:pk>/', views.AutorDetail.as_view(), name=views.AutorDetail.name),
    path('user/', views.UserList.as_view(), name=views.UserList.name),
    path('user/<int:pk>/', views.UserDetail.as_view(), name=views.UserDetail.name),
    path('kategoria/', views.KategoriaList.as_view(), name=views.KategoriaList.name),
    path('kategoria/<int:pk>/', views.KategoriaDetail.as_view(), name=views.KategoriaDetail.name),
    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),
]
