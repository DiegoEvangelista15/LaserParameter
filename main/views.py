from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

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
