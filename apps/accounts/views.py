from multiprocessing import context
import re
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.shortcuts import get_object_or_404
from spending.models import Spending_Accounts
from accounts.models import User as Accounts

def login(request):
    #Se a requsiçao passada for post
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        #Com os dados passados, verifcar se é possível autenticar o usuário
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user) #loga o usuário
            return redirect('home')
        else:
            #se nao atenticar, é porque o ussuário ou senha está erradp
            messages.error(request, 'Usuário ou senha incorreto!') 
            return redirect('index')
    else:
        # Se arequisição nao for post
        return render(request, 'login.html')
    
def home(request):
    # se o usuário estiver logado
    if request.user.is_authenticated:
        # Acessar informações do usuário
        try:
            accounts = get_object_or_404(Accounts, user=request.user)
            spending = Spending_Accounts.objects.filter(accounts = accounts)
            return render(request, 'home.html', {'spending':spending})
        except:
            return redirect('index')
    else:
        messages.error(request, 'Usuário não autenticado. Faça o login para acessar a pagina desejada.')
        return redirect('index')