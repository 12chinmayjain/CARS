from django.contrib import admin
from .models import Info


# Register your models here.
@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'password')
