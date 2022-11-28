from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib import auth, messages



def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == "POST":
        usuario = request.POST['usuario']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password2 == '1234':
            if usuario == '' or password == '':
                return redirect('index')
            user = auth.authenticate(request, username=usuario, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('main_page')
    return render(request, 'index.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

def conta_usuario(request):
    return render(request, 'conta_usuario.html')

def criar_usuario(request):
    ...

def main_page(request):
    return render(request, 'pagina_principal.html')

#TODO criar o criar conta e corrigir os htmls
def criar_conta(request):
    return render(request, 'criar_conta.html')

#TODO criar o criar parâmetro
def criar_param(request):
    return render(request, 'criar_param.html')

def editar_excluir(request):
    return render(request, 'editar_excluir.html')

def listar_param(request):
    return render(request, 'listar_param.html')
