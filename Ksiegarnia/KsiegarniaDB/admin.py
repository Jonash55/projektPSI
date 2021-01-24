from django.contrib import admin
from .models import User, Autor, Ksiazka, Kategoria, Paragon, Adres
from .forms import UserChangeForm, UserCreationForm
from django.contrib.auth.admin import UserAdmin
# Register your models here.


class UserAdminCustom(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'idUsera', 'is_active', 'is_staff', 'is_admin')
    list_filter = ('idUsera', 'email')
    search_filter = ('idUsera', 'email')
    ordering = ['email']

    fieldsets = (
        (None, {'fields': ('email', 'is_active', 'is_staff', 'is_admin', 'password')}),
        ('Groups', {'fields': ('groups',)}),
        ('Permissions', {'fields': ('user_permissions',)})
    )

    add_fieldsets = (
        (None, {'fields': ('email', 'is_active', 'is_staff', 'is_admin', 'password')}),
        ('Groups', {'fields': ('groups',)}),
        ('Permissions', {'fields': ('user_permissions',)})
    )


admin.site.register(User, UserAdminCustom)
admin.site.register(Autor)
admin.site.register(Ksiazka)
admin.site.register(Kategoria)
admin.site.register(Paragon)
admin.site.register(Adres)
