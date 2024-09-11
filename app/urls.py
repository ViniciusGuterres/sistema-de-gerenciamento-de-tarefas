from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='app'),
    path('', views.lista_tarefa, name='lista_tarefa'),
    path('criar_tarefa/', views.criar_tarefa, name='criar_tarefa'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
