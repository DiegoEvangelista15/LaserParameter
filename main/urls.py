from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('main_page/', views.main_page, name='main_page'),
    path('criar_usuario/', views.criar_usuario, name='criar_usuario'),
    path('criar_param/', views.criar_param, name='criar_param'),
    path('listar_param/', views.listar_param, name='listar_param'),
    path('logout/', views.logout, name='logout'),
    path('login/', views.login, name='login'),
    path('conta_usuario/', views.conta_usuario, name='conta_usuario'),
    path('acessar_para/<int:para_id>', views.acessar_para, name='acessar_para'),
    path('delete_para/<int:delete_id>', views.delete_para, name='delete_para'),
    path('edita_para/<int:edita_id>', views.edita_para, name='edita_para'),
    path('atualiza_para/', views.atualiza_para, name='atualiza_para'),
]
