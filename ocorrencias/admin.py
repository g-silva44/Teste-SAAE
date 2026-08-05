from django.contrib import admin
from .models import Bairro, Ocorrencia

@admin.register(Bairro)
class BairroAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'latitude', 'longitude')
    search_fields = ('nome',)

@admin.register(Ocorrencia)
class OcorrenciaAdmin(admin.ModelAdmin):
    list_display = ('id', 'bairro', 'data_hora', 'status', 'responsavel')
    list_filter = ('status', 'bairro')
    search_fields = ('bairro__nome', 'descricao', 'responsavel__username')
