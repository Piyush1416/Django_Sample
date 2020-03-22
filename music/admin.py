from django.contrib import admin

# Register your models here.

from .models import Albumn, Song

admin.site.register(Albumn)
admin.site.register(Song)