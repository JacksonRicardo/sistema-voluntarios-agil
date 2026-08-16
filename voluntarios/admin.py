from django.contrib import admin
from .models import Voluntario

@admin.register(Voluntario)
class VoluntarioAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'email', 'area_atuacao', 'ativo', 'data_cadastro')
    list_filter = ('area_atuacao', 'ativo')
    search_fields = ('nome_completo', 'email')
    ordering = ('-data_cadastro',)
