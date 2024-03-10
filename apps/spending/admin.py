from django.contrib import admin
from .models import Spending, Spending_Accounts

# Register your models here.
admin.site.register(Spending)
admin.site.register(Spending_Accounts)
