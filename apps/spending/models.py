from django.db import models
from accounts.models import User
from django.utils import timezone

# Create your models here.

class Spending(models.Model):

    SPEND_TYPES = [
        ('MERCADO','Mercado'),
        ('CASA','Casa'),
        ]
    
    type = models.CharField('Tipo', max_length=100, choices=SPEND_TYPES, default='', null=False)
    title = models.CharField("Título", max_length=100, blank=False, null=False)
    value = models.FloatField('Valor', null=False, blank=False, default=0.0)
    divided_accounts = models.ManyToManyField(User, related_name='divided_spending_set', verbose_name='Conta(s) Dividida(s)')
    voucher = models.FileField('Comprovante', upload_to="images/", blank=True)
    description = models.TextField('Descrição', null=True, blank=True)
    registrar = models.ForeignKey(User, on_delete=models.CASCADE, related_name='registered_spending_set', null=False, blank=False, verbose_name='Regitrador')
    created_at = models.DateTimeField('Criado em', default=timezone.now)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Gasto'
        verbose_name_plural = 'Gastos'


class Spending_Accounts(models.Model):

    SPEND_STATUS = [
        ('PAGO','Pago'),
        ('PENDENTE','Pendente'),
        ]
    
    spending = models.ForeignKey(Spending, on_delete=models.CASCADE, verbose_name='Gasto Relacionado')
    accounts = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Conta Relacionada')
    status = models.CharField('Status', max_length=100, choices=SPEND_STATUS, default='')
    value = models.FloatField('Valor', null=False, blank=False, default=0.0)
    
    def __str__(self):
        return self.status

    class Meta:
        verbose_name = 'Gasto do usuário'
        verbose_name_plural = 'Gasto dos usuários'