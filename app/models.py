from django.db import models
from django.utils import timezone
from django.contrib.auth.hashers import make_password, check_password

class Usuario(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nome")
    email = models.EmailField(unique=True, verbose_name="E-mail")
    password = models.CharField(max_length=128, verbose_name="Senha")

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
    
    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.email
    
class Tarefa(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('em_progresso', 'Em Progresso'),
        ('concluida', 'Concluída'),
    ]

    titulo = models.CharField(max_length=255, verbose_name="Título")
    descricao = models.TextField(verbose_name="Descrição", blank=True)
    data_criacao = models.DateTimeField(default=timezone.now, verbose_name="Data de Criação")
    data_vencimento = models.DateTimeField(verbose_name="Data de Vencimento", null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente', verbose_name="Status")
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='tarefas', verbose_name="Usuário")

    def __str__(self):
        return self.titulo
