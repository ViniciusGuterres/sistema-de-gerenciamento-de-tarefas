from django import forms
from .models import Tarefa

class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ['titulo', 'descricao', 'data_criacao', 'data_vencimento', 'status', 'usuario']
        widgets = {
            'data_vencimento': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }