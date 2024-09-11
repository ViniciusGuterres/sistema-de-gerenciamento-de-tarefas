from django.shortcuts import render, redirect
from .models import Tarefa
from .forms import TarefaForm
from django.contrib.auth import authenticate, login as auth_login
from .forms import UsuarioCadastroForm, CustomLoginForm

def cadastro(request):
    if request.method == 'POST':
        form = UsuarioCadastroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UsuarioCadastroForm()
    
    return render(request, 'cadastro.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                auth_login(request, user) 
                return redirect('lista_tarefa')
            else:
                form.add_error(None, 'Invalid credentials')
    else:
        form = CustomLoginForm()

    return render(request, 'login.html', {'form': form})

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
        form = TarefaForm()
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
