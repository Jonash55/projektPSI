from django.db import models


class Autor(models.Model):
    idAutora = models.IntegerField(primary_key=True)
    Imie = models.CharField(max_length=75)
    Nazwisko = models.CharField(max_length=75)
    DataUrodzenia = models.DateTimeField()
    Opis = models.CharField(max_length=250)


statusdowyboru = (
    ('prac', 'pracownik'),
    ('kier', 'kierownik')
)


class User(models.Model):
    idUsera = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=32)
    email = models.CharField(max_length=255)
    status = models.CharField(max_length=4, choices=statusdowyboru)


class Klient(models.Model):
    idKlienta = models.IntegerField(primary_key=True)
    Imie = models.CharField(max_length=45)
    Nazwisko = models.CharField(max_length=45)
    czyUser = models.BooleanField()


class Adres(models.Model):
    idAdresu = models.IntegerField(primary_key=True)
    Miasto = models.CharField(max_length=45)
    Ulica = models.CharField(max_length=45)
    KodPocztowy = models.CharField(max_length=45)
    Wojewodztwo = models.CharField(max_length=45)
    User.idUsera = models.ManyToManyField(User)
    Klient.idKlienta = models.ManyToManyField(Klient)


class Kategoria(models.Model):
    idKategorii = models.IntegerField(primary_key=True)
    Nazwa = models.CharField(max_length=45)
    Opis = models.CharField(max_length=155)


class Paragon(models.Model):
    idParagonu = models.IntegerField(primary_key=True)
    User.idUsera = models.IntegerField()
    Klient.idKlienta = models.ForeignKey(Klient, on_delete=models.CASCADE)
    suma = models.FloatField()


class Ksiazka(models.Model):
    idKsiazki = models.IntegerField(primary_key=True)
    Autor.idAutora = models.ForeignKey(Autor, on_delete=models.CASCADE)
    Kategoria.idKategorii = models.ForeignKey(Kategoria, on_delete=models.CASCADE)
    tytul = models.CharField(max_length=150)
    cena_netto = models.FloatField()
    rok_wydania = models.DateTimeField()
    cena_brutto = models.FloatField()
    ilosc = models.CharField(max_length=45)
