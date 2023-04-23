from django.contrib import admin
from .models import Autor, Kniha, Vydavatelstvi, Zanr, Recenze

admin.site.register(Autor)
admin.site.register(Kniha)
admin.site.register(Vydavatelstvi)
admin.site.register(Zanr)
admin.site.register(Recenze)