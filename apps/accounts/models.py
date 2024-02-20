from django.db import models

class Accounts(models.Model):
    name = models.CharField('Nome', max_length=50)
    description = models.TextField('Descricao', max_length=100)
    
    class Meta:
        verbose_name = 'Contas'
        verbose_name_plural = 'Contas'
        ordering =['id']

    def __str__(self):
        return self.name
