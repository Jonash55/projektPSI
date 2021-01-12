from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser


class Autor(models.Model):
    idAutora = models.AutoField(primary_key=True)
    Imie = models.CharField(max_length=75)
    Nazwisko = models.CharField(max_length=75)
    DataUrodzenia = models.DateTimeField()
    Opis = models.CharField(max_length=250)

    def __str__(self):
        return self.Imie + ' ' + self.Nazwisko + ' ' + str(self.DataUrodzenia)


class CustomUserManager(BaseUserManager):
    def create_user(self, email, idUsera, password=None):
        if not email:
            raise ValueError("User musi mieć email")
        if not password:
            raise ValueError("User musi mieć hasło")
        user = self.model(
            email=self.normalize_email(email)
        )
        user.idUsera = idUsera
        user.set_password(password)
        user.is_admin = False
        user.is_staff = False
        user.save(using=self._db)
        return user

    def create_superuser(self, email, idUsera, password=None):
        if not email:
            raise ValueError("SuperUser musi mieć email")
        if not password:
            raise ValueError("SuperUser musi mieć hasło")
        user = self.model(
            email=self.normalize_email(email)
        )
        user.idUsera = idUsera
        user.set_password(password)
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_stuffuser(self, email, idUsera, password=None):
        if not email:
            raise ValueError("StaffUser musi mieć email")
        if not password:
            raise ValueError("StaffUser musi mieć hasło")
        user = self.model(
            email=self.normalize_email(email)
        )
        user.idUsera = idUsera
        user.set_password(password)
        user.is_admin = False
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    ADMIN = 'admin'
    STAFF = 'staff'
    STATUS = [
        (ADMIN, _('Admin user')),
        (STAFF, _('Staff user')),
    ]
    email = models.EmailField(_('email'), unique=True)
    idUsera = models.AutoField(primary_key=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['idUsera']

    objects = CustomUserManager()

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def __str__(self):
        return "{}".format(self.email)


class Klient(models.Model):
    idKlienta = models.AutoField(primary_key=True)
    Imie = models.CharField(max_length=45)
    Nazwisko = models.CharField(max_length=45)

    class Meta:
        ordering = ('idKlienta',)

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

    class Meta:
        ordering = ('idAdresu',)

    def __str__(self):
        return self.Miasto + ' ' + self.Ulica + ' ' + self.Wojewodztwo


class Kategoria(models.Model):
    idKategorii = models.AutoField(primary_key=True)
    Nazwa = models.CharField(max_length=45)
    Opis = models.CharField(max_length=500)

    class Meta:
        ordering = ('idKategorii',)

    def __str__(self):
        return self.Nazwa + ' ' + self.Opis


class Paragon(models.Model):
    idParagonu = models.AutoField(primary_key=True)
    idUsera = models.ForeignKey(User, related_name='paragon', on_delete=models.SET_NULL, null=True)
    idKlienta = models.ForeignKey(Klient, related_name='paragon', on_delete=models.SET_NULL, null=True)
    suma = models.FloatField()
    dataWystawienia = models.DateTimeField(null=True)

    class Meta:
        ordering = ('idParagonu',)

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

    class Meta:
        ordering = ('idKsiazki',)

    def __str__(self):
        return self.tytul + ' ' + str(self.cena_netto) + ' ' + str(self.rok_wydania) + ' ' + str(self.cena_brutto)\
               + ' ' + str(self.ilosc)
