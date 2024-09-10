from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='app'),
    path('lista_tarefa/', views.lista_tarefa, name='lista_tarefa'),
    path('criar_tarefa/', views.criar_tarefa, name='criar_tarefa'),
]