from django.urls import path
from . import views

urlpatterns = [
    path('lista_tarefa', views.lista_tarefa, name='lista_tarefa'),
    path('atualizar_tarefa/<int:tarefa_id>/', views.atualizar_tarefa, name='atualizar_tarefa'),
    path('deletar_tarefa/<int:tarefa_id>/', views.deletar_tarefa, name='deletar_tarefa'),
    path('criar_tarefa/', views.criar_tarefa, name='criar_tarefa'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]