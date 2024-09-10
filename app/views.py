from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarefa
from .forms import TarefaForm

def lista_tarefa(request):
    Tarefas = Tarefa.objects.all()
    return render(request, 'lista_tarefa.html', {'Tarefas': Tarefas})

def criar_tarefa(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_tarefa')
    else:
        form = TarefaForm()  # Correct initialization in GET requests
    return render(request, 'tarefa_form.html', {'form': form})


# def Tarefa_update(request, Tarefa_id):
#     Tarefa = get_object_or_404(Tarefa, id=Tarefa_id)
#     if request.method == 'POST':
#         form = TarefaForm(request.POST, instance=Tarefa)
#         if form.is_valid():
#             form.save()
#             return redirect('lista_tarefa')
#     else:
#         form = TarefaForm(instance=Tarefa)
#     return render(request, 'Tarefas/Tarefa_form.html', {'form': form})

# def Tarefa_delete(request, Tarefa_id):
#     Tarefa = get_object_or_404(Tarefa, id=Tarefa_id)
#     if request.method == 'POST':
#         Tarefa.delete()
#         return redirect('lista_tarefa')
#     return render(request, 'Tarefas/Tarefa_confirm_delete.html', {'Tarefa': Tarefa})
