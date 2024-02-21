from django.db import models
from django.contrib.auth.models import User


class User(models.Model):
    first_name = models.CharField('Nome', max_length=50)
    last_name = models.CharField('Sobrenome', max_length=100) 
    email = models.EmailField('E-mail', null=True, blank=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.first_name
