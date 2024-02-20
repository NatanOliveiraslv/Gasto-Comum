from multiprocessing import context
import re
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import get_object_or_404

def login(request):
    #Se a requsiçao passada for post
    if request.method == "POST":
        usuario = request.POST.get("usuario")
        senha = request.POST.get("senha")
        #Com os dados passados, verifcar se é possível autenticar o usuário
        user = authenticate(username=usuario, password=senha)
        if user is not None:
            login(request, user) #loga o usuário
            return redirect('painel') # redireciona para o link /painel
        else:
            #se nao atenticar, é porque o ussuário ou senha está erradp
            messages.error(request, 'Usuário ou senha incorreto!') 
            return redirect('index')
    else:
        # Se arequisição nao for post
        return render(request, 'login/login.html')