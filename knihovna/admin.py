from django.contrib import admin
from .models import Autor, Kniha, Vydavatelstvi, Zanr

admin.site.register(Autor)
admin.site.register(Kniha)
admin.site.register(Vydavatelstvi)
admin.site.register(Zanr)