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
            titulo = request.POST.get("titulo")
            descricao = request.POST.get("descricao")
            professor_autenticado = Professor.objects.get(user=User.objects.get(username=usuario)) #atribui a varaivel o professor autenticado
            materia = Materia.objects.get(professor = professor_autenticado) #atribui a varaivel a materia do profeesor autenticado
            # cria uma nova atividade
            nova_atividade = Atividade.objects.create(
                titulo=titulo,
                descricao=descricao,
                materia=materia,
                turma=turma,
            )

            nova_atividade.save()
            messages.success(request, 'Atividade cadastrada com sucesso!') 
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