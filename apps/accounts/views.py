from multiprocessing import context
import re
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.shortcuts import get_object_or_404

def login(request):
    #Se a requsiçao passada for post
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        #Com os dados passados, verifcar se é possível autenticar o usuário
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user) #loga o usuário
            messages.error(request, 'Parabens, voce está logado!') 
            return redirect('home')
        else:
            #se nao atenticar, é porque o ussuário ou senha está erradp
            messages.error(request, 'Usuário ou senha incorreto!') 
            return redirect('index')
    else:
        # Se arequisição nao for post
        return render(request, 'login.html')
    
def home(request):
    return render(request, 'home.html')