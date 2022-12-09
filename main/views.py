from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib import auth, messages
from django.contrib.auth.models import User
from main.models import Parameter



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
    if request.method == 'POST':
        usuario = request.POST['username']
        email = request.POST['email']
        senha01 = request.POST['password']
        senha02 = request.POST['password2']

        if senha01 != senha02:
            return redirect('conta_usuario')
        user = User.objects.create_user(username=usuario, email=email, password=senha01)
        user.is_staff = True
        user.save()
        return redirect('index')
    return redirect('conta_usuario')

def main_page(request):
    return render(request, 'pagina_principal.html')

#TODO criar o criar parâmetro usar o FORM do Django
def criar_param(request):
    return render(request, 'criar_param.html')


def listar_param(request):
    parameter = Parameter.objects.all()
    return render(request, 'listar_param.html', {'parameter': parameter})

#TODO colocar as unidades
def acessar_para(request, para_id):
    para = get_object_or_404(Parameter, pk=para_id)
    para_acessar = {'para': para}
    return render(request, 'acessar_para.html', para_acessar)


