from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User




@admin.register(User)
class UserAdm(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password', 'equipo')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
