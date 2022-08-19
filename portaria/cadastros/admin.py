from django.contrib import admin
from .models import Casa, Morador, Visitante, PrestadorServico

# Register your models here.

admin.site.register(Casa)
admin.site.register(Morador)
admin.site.register(Visitante)
admin.site.register(PrestadorServico)