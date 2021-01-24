from rest_framework import serializers
from .models import Autor, User, Ksiazka, Adres, Kategoria, Paragon
import datetime


class AutorSerializer(serializers.HyperlinkedModelSerializer):
    ksiazka = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='ksiazka-detail')

    class Meta:
        model = Autor
        fields = ["idAutora", "url", "Imie", "Nazwisko", "DataUrodzenia", "Opis", "ksiazka"]
        read_only_fields = ["idAutora"]


class UserAdresSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Adres
        fields = ['url', 'Ulica', 'Miasto']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    paragon = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='paragon-detail')
    adresy = UserAdresSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ["idUsera", "url", "email", "password", "is_admin", "is_staff", "is_active", 'paragon', 'adresy']
        read_only_fields = ["idUsera"]


class AdresSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Adres
        fields = ["idAdresu", "url", "Miasto", "Ulica", "KodPocztowy", "Wojewodztwo", "idUsera", "owner"]
        read_only_fields = ["idAdresu", "idUsera"]


class KategoriaSerializer(serializers.HyperlinkedModelSerializer):
    ksiazka = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='ksiazka-detail')

    class Meta:
        model = Kategoria
        fields = ["idKategorii", "url", "Nazwa", "Opis", "ksiazka"]
        read_only_fields = ["idKategorii"]


class ParagonSerializer(serializers.HyperlinkedModelSerializer):
    idUsera = serializers.HyperlinkedRelatedField(read_only=True, view_name='user-detail')

    class Meta:
        model = Paragon
        fields = ["idParagonu", "url", "idUsera", "suma", "dataWystawienia"]
        read_only_fields = ["idParagonu", "idUsera"]

    def validate_suma(self, value):
        if value < 0:
            raise serializers.ValidationError("Suma nie może być mniejsza od 0")
        return value

    def validate_dataWystawienia(self, value):
        value = datetime.datetime.strptime(value, "%d/%m/%Y")
        if value > datetime.datetime.now():
            raise serializers.ValidationError("Data wystawienia jest niepoprawna (nowsza niż dzień dzisiejszy)")
        return value


class KsiazkaSerializer(serializers.HyperlinkedModelSerializer):
    idAutora = serializers.SlugRelatedField(queryset=Autor.objects.all(), slug_field='Nazwisko')
    idKategorii = serializers.SlugRelatedField(queryset=Kategoria.objects.all(), slug_field='Nazwa')

    class Meta:
        model = Ksiazka
        fields = ["idKsiazki", "url", "idAutora", "idKategorii", "tytul", "cena_netto", "rok_wydania", "cena_brutto",
                  "ilosc"]
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
