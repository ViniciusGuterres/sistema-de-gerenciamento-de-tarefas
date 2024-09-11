from django import forms
from .models import Tarefa, Usuario
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate

class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ['titulo', 'descricao', 'data_criacao', 'data_vencimento', 'status', 'usuario']
        widgets = {
            'data_vencimento': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class UsuarioCadastroForm(forms.ModelForm):
    password1 = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={'class': 'form-input mt-1 block w-full'})
    )
    password2 = forms.CharField(
        label='Confirme a Senha',
        widget=forms.PasswordInput(attrs={'class': 'form-input mt-1 block w-full'})
    )

    class Meta:
        model = Usuario
        fields = ['email', 'name']  # Verifique se 'name' está correto
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input mt-1 block w-full'}),
            'email': forms.EmailInput(attrs={'class': 'form-input mt-1 block w-full'}),
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("As senhas não coincidem")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class CustomLoginForm(forms.Form):
    email = forms.CharField()  # Altere 'username' para 'email'
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')  # Altere 'username' para 'email'
        password = cleaned_data.get('password')
        print(email)  # Verifique se o 'email' está correto
        print(password)

        if email and password:
            self.user = authenticate(self.request, username=email, password=password)  # Use 'username=email'
            if self.user is None:
                raise forms.ValidationError("Nome de usuário ou senha inválidos")
        return cleaned_data

    def get_user(self):
        return getattr(self, 'user', None)
