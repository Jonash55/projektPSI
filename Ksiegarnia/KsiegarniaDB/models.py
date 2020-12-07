from django.db import models


class Autor(models.Model):
    idAutora = models.AutoField(primary_key=True)
    Imie = models.CharField(max_length=75)
    Nazwisko = models.CharField(max_length=75)
    DataUrodzenia = models.DateTimeField()
    Opis = models.CharField(max_length=250)

    def __str__(self):
        return self.Imie + ' ' + self.Nazwisko + ' ' + str(self.DataUrodzenia)


statusdowyboru = (
    ('prac', 'pracownik'),
    ('kier', 'kierownik')
)


class User(models.Model):
    idUsera = models.AutoField(primary_key=True)
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=32)
    email = models.EmailField(null=True)
    status = models.CharField(max_length=4, choices=statusdowyboru)


class Klient(models.Model):
    idKlienta = models.AutoField(primary_key=True)
    Imie = models.CharField(max_length=45)
    Nazwisko = models.CharField(max_length=45)
    czyUser = models.BooleanField()

    def __str__(self):
        return self.Imie + ' ' + self.Nazwisko


class Adres(models.Model):
    idAdresu = models.AutoField(primary_key=True)
    Miasto = models.CharField(max_length=45)
    Ulica = models.CharField(max_length=100)
    KodPocztowy = models.CharField(max_length=45)
    Wojewodztwo = models.CharField(max_length=45)
    idUsera = models.ManyToManyField(User, related_name='adres')
    idKlienta = models.ManyToManyField(Klient, related_name='adres')

    def __str__(self):
        return self.Miasto + ' ' + self.Ulica + ' ' + self.Wojewodztwo


class Kategoria(models.Model):
    idKategorii = models.AutoField(primary_key=True)
    Nazwa = models.CharField(max_length=45)
    Opis = models.CharField(max_length=500)

    def __str__(self):
        return self.Nazwa + ' ' + self.Opis


class Paragon(models.Model):
    idParagonu = models.AutoField(primary_key=True)
    idUsera = models.ForeignKey(User, related_name='paragon', on_delete=models.SET_NULL, null=True)
    idKlienta = models.ForeignKey(Klient, related_name='paragon', on_delete=models.SET_NULL, null=True)
    suma = models.FloatField()
    dataWystawienia = models.DateTimeField(null=True)

    def __str__(self):
        return str(self.suma) + ' ' + str(self.dataWystawienia)


class Ksiazka(models.Model):
    idKsiazki = models.AutoField(primary_key=True)
    idAutora = models.ForeignKey(Autor, related_name='ksiazka', on_delete=models.SET_NULL, null=True)
    idKategorii = models.ForeignKey(Kategoria, related_name='ksiazka', on_delete=models.SET_NULL, null=True)
    tytul = models.CharField(max_length=150)
    cena_netto = models.FloatField()
    rok_wydania = models.DateTimeField()
    cena_brutto = models.FloatField()
    ilosc = models.CharField(max_length=45)

    def __str__(self):
        return self.tytul + ' ' + str(self.cena_netto) + ' ' + str(self.rok_wydania) + ' ' + str(self.cena_brutto)\
               + ' ' + str(self.ilosc)
