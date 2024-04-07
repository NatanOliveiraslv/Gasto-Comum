from django.shortcuts import redirect, render
from django.contrib import messages
from django.shortcuts import get_object_or_404
from spending.models import Spending_Accounts, Spending
from accounts.models import User as Accounts
from .forms import SpendingForm


def open_spend(request, spending_id):
    # se o usuário estiver logado
    if request.user.is_authenticated:
        spending = get_object_or_404(Spending_Accounts, pk=spending_id)
        if request.method == "POST":
            if spending.status != "PAGO":
                spending.status = "PAGO"
                spending.save()
                return redirect('open_spend', spending_id)
        else:
            try:
                return render(request, 'open_spend.html', {'spending':spending})
            except:
                messages.error(request, "Ops... Algo deu errado :(")
                return redirect('index')
    else:
        messages.error(request, 'Usuário não autenticado. Faça o login para acessar a pagina desejada.')
        return redirect('index')

def registration_spend(request):
    if request.user.is_authenticated:
        if request.method == "POST":

            accounts = get_object_or_404(Accounts, user=request.user) 
            divided_accounts =  Accounts.objects.filter(email__in=request.POST.getlist("emails"))
            
            spending = Spending.objects.create(
                type=request.POST.get("type"),
                title=request.POST.get("title"),
                value=request.POST.get("value"),
                description=request.POST.get("description"), 
                registrar=accounts,
            )
            spending.save()

            if request.FILES.get('voucher') is not None:  
                spending.voucher = request.FILES.get('voucher')  
                spending.save()

            spending.divided_accounts.set(divided_accounts)
            
            registration_spending_accounts(spending)

            messages.success(request, 'Gasto cadastrado com sucesso!')
            return redirect('registration_spend')
        else:
            try:
                form = SpendingForm()
                return render(request, 'registration_spend.html', {"form": form})
            except:
                messages.error(request, "Ops... Algo deu errado :(")
                return redirect('index')
    else:
        messages.error(request, 'Usuário não autenticado. Faça o login para acessar a pagina desejada.')
        return redirect('index')

def registration_spending_accounts(spending):
    accounts = spending.divided_accounts.all()
    value = float(spending.value) / len(accounts)

    for account in accounts:
        spending_accounts = Spending_Accounts.objects.create(
            spending=spending,
            accounts=account,
            status='PENDENTE',
            value=value,
        )
        spending_accounts.save()