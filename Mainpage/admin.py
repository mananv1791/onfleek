from django.contrib import admin
from .models import Dress


@admin.register(Dress)
class DressAdmin(admin.ModelAdmin):
    pass
