from django.db import models


class Autor(models.Model):
    idAutora = models.AutoField(primary_key=True)
    Imie = models.CharField(max_length=75)
    Nazwisko = models.CharField(max_length=75)
    DataUrodzenia = models.DateTimeField()
    Opis = models.CharField(max_length=250)


statusdowyboru = (
    ('prac', 'pracownik'),
    ('kier', 'kierownik')
)


class User(models.Model):
    idUsera = models.AutoField(primary_key=True)
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=32)
    email = models.EmailField(null=True)
    email2 = models.EmailField(null=True)
    status = models.CharField(max_length=4, choices=statusdowyboru)


class Klient(models.Model):
    idKlienta = models.AutoField(primary_key=True)
    Imie = models.CharField(max_length=45)
    Nazwisko = models.CharField(max_length=45)
    czyUser = models.BooleanField()


class Adres(models.Model):
    idAdresu = models.AutoField(primary_key=True)
    Miasto = models.CharField(max_length=45)
    Ulica = models.CharField(max_length=100)
    KodPocztowy = models.CharField(max_length=45)
    Wojewodztwo = models.CharField(max_length=45)
    idUsera = models.ManyToManyField(User)
    idKlienta = models.ManyToManyField(Klient)


class Kategoria(models.Model):
    idKategorii = models.AutoField(primary_key=True)
    Nazwa = models.CharField(max_length=45)
    Opis = models.CharField(max_length=500)


class Paragon(models.Model):
    idParagonu = models.AutoField(primary_key=True)
    idUsera = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    idKlienta = models.ForeignKey(Klient, on_delete=models.CASCADE, null=True)
    suma = models.FloatField()


class Ksiazka(models.Model):
    idKsiazki = models.AutoField(primary_key=True)
    idAutora = models.ForeignKey(Autor, on_delete=models.CASCADE, null=True)
    idKategorii = models.ForeignKey(Kategoria, on_delete=models.CASCADE, null=True)
    tytul = models.CharField(max_length=150)
    cena_netto = models.FloatField()
    rok_wydania = models.DateTimeField()
    cena_brutto = models.FloatField()
    ilosc = models.CharField(max_length=45)
