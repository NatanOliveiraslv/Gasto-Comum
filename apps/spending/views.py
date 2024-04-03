from django.shortcuts import redirect, render
from django.contrib import messages
from django.shortcuts import get_object_or_404
from spending.models import Spending_Accounts
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
            form = SpendingForm(request.POST, request.FILES)

            if form.is_valid():
                # Salve o objeto Spending com base nos dados do formulário
                spending = form.save(commit=False)
                spending.registrar = accounts # Atribua o usuário atual como o registrador
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
    print(spending.divided_accounts.all())