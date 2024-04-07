from django.contrib import admin
from .models import Spending, Spending_Accounts

# Register your models here.
admin.site.register(Spending)

def marcar_como_pago(modeladmin, request, queryset):
    queryset.update(status='PAGO')

marcar_como_pago.short_description = "Marcar como Pago"  # Descrição da ação

def marcar_como_pendente(modeladmin, request, queryset):
    queryset.update(status='PENDENTE')

marcar_como_pendente.short_description = "Marcar como Pendente"  # Descrição da ação

class GastoAdmin(admin.ModelAdmin):
    list_display = ['id', 'spending', 'accounts', 'status', 'value']
    actions = [marcar_como_pago, marcar_como_pendente]  # Adiciona a ação personalizada ao admin

admin.site.register(Spending_Accounts, GastoAdmin)
