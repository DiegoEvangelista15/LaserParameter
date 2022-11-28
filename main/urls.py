from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('main_page/', views.main_page, name='main_page'),
    path('criar_usuario/', views.criar_usuario, name='criar_usuario'),
    path('criar_param/', views.criar_param, name='criar_param'),
    path('editar_excluir/', views.editar_excluir, name='editar_excluir'),
    path('listar_param/', views.listar_param, name='listar_param'),
    path('logout/', views.logout, name='logout'),
    path('login/', views.login, name='login'),
    path('conta_usuario/', views.conta_usuario, name='conta_usuario'),
]
