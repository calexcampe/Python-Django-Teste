from django.contrib import admin
from core.models import Evento
# Register your models here.

class Eventoadmin(admin.ModelAdmin): #uma classe para mostrar quais campos da tabela quero que apareça no grid
    list_display = ('titulo', 'data_evento', 'data_criacao')
    #list_filter = para criar um filtro de pesquisa

admin.site.register(Evento, Eventoadmin) # registro a classe em meu admin a classe evento é do models pois
                                            # é uma classe de banco de dados