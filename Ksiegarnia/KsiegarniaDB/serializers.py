from rest_framework import serializers
from rest_framework.serializers import ValidationError
from .models import Autor, User, Ksiazka, Klient, Adres, Kategoria, Paragon
import datetime


class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = ["idAutora", "Imie", "Nazwisko", "DataUrodzenia", "Opis"]
        read_only_fields = ["idAutora"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["idUsera", "username", "password", "email", "status"]
        read_only_fields = ["idUsera"]


class KlientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Klient
        fields = ["idKlienta", "Imie", "Nazwisko", "czyUser"]
        read_only_fields = ["idKlienta"]


class AdresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adres
        fields = ["idAdresu", "Miasto", "Ulica", "KodPocztowy", "Wojewodztwo", "idUsera", "idKlienta"]
        read_only_fields = ["idAdresu", "idUsera", "idKlienta"]


class KategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kategoria
        fields = ["idKategorii", "Nazwa", "Opis"]
        read_only_fields = ["idKategorii"]


class ParagonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paragon
        fields = ["idParagonu", "idUsera", "idKlienta", "suma", "dataWystawienia"]
        read_only_fields = ["idParagonu", "idUsera", "idKlienta"]

    def validate_suma(self, value):
        if value < 0:
            raise serializers.ValidationError("Suma nie może być mniejsza od 0")
        return value

    def validate_dataWystawienia(self, value):
        value = datetime.datetime.strptime(value, "%d/%m/%Y")
        if value > datetime.datetime.now():
            raise serializers.ValidationError("Data wystawienia jest niepoprawna (nowsza niż dzień dzisiejszy)")
        return value


class KsiazkaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ksiazka
        fields = ["idKsiazki", "idAutora", "idKategorii", "tytul", "cena_netto", "rok_wydania", "cena_brutto", "ilosc"]
        read_only_fields = ["idKsiazki", "idAutora", "idKategorii"]

    def validate_cena_netto(self, value):
        if value < 0:
            raise serializers.ValidationError("Cena netto nie może być mniejsza od 0")
        return value

    def validate_cena_brutto(self, value):
        if value < 0:
            raise serializers.ValidationError("Cena brutto nie może być mniejsza od 0")
        return value

    def validate(self, data):
        if data["cena_netto"] > data["cena_brutto"]:
            raise serializers.ValidationError("Cena netto nie może być większa od ceny brutto")
        return data

    def validate_rok_wydania(self, value):
        value = datetime.datetime.strptime(value, "%d/%m/%Y")
        if value > datetime.datetime.now():
            raise serializers.ValidationError("Data wydania jest niepoprawna (nowsza niż dzień dzisiejszy)")
        return value

    def validate_ilosc(self, value):
        if value < 0:
            raise serializers.ValidationError("Ilość mniejsza od 0")
        return value
