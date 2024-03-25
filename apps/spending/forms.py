# forms.py
from django import forms
from .models import Spending

class SpendingForm(forms.ModelForm):
    class Meta:
        model = Spending
        fields = ['type', 'title', 'value', 'divided_accounts', 'voucher', 'description']
        labels = {
            'type': 'Tipo',
            'title': 'Título',
            'value': 'Valor',
            'divided_accounts': 'Conta(s) Dividida(s)',
            'voucher': 'Comprovante',
            'description': 'Descrição',
        }
        widgets = {
            'type': forms.Select(choices=Spending.SPEND_TYPES),
            'voucher': forms.ClearableFileInput(attrs={'multiple': True}),  # Para permitir múltiplos uploads de arquivos
            'divided_accounts': forms.CheckboxSelectMultiple(),  # Para permitir seleção múltipla de contas divididas
        }
