from rest_framework import serializers
from rest_framework.serializers import ValidationError
from .models import Autor, User, Ksiazka, Klient, Adres, Kategoria, Paragon


class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model: Autor
        fields = ["idAutora", "Imie", "Nazwisko", "DataUrodzenia", "Opis"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model: User
        fields = ["idUsera", "username", "password", "email", "email2", "status"]

    def create(self, validated_data):
        print(validated_data)
        username = validated_data['username']
        password = validated_data['password']
        email = validated_data['email']
        email2 = validated_data['email2']
        user_obj = User(
            username=username,
            email=email,
            email2=email2,
        )
        user_obj.save(password)
        user_obj.save()
        return validated_data

    def validate_email(self, value):
        data = self.get_initial()
        email = data.get("email2")
        email2 = value
        if email != email2:
            raise ValidationError("Email'e muszą się zgadzać")
        return value

    def validate_email2(self, value):
        data = self.get_initial()
        email = data.get("email")
        email2 = value
        if email != email2:
            raise ValidationError("Email'e muszą się zgadzać")
        return value


class KlientSerializer(serializers.ModelSerializer):
    class Meta:
        model: Klient
        fields = ["idKlienta", "Imie", "Nazwisko", "czyUser"]


class AdresSerializer(serializers.ModelSerializer):
    class Meta:
        model: Adres
        fields = ["idAdresu", "Miasto", "Ulica", "KodPocztowy", "Wojewodztwo", "idUsera", "idKlienta"]


class KategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model: Kategoria
        fields = ["idKategorii", "Nazwa", "Opis"]


class ParagonSerializer(serializers.ModelSerializer):
    class Meta:
        model: Paragon
        fields = ["idParagonu", "idUsera", "idKlienta", "suma"]


class KsiazkaSerializer(serializers.ModelSerializer):
    class Meta:
        model: Ksiazka
        fields = ["idKsiazki", "idAutora", "idKategorii", "tytul", "cena_netto", "rok_wydania", "cena_brutto", "ilosc"]
