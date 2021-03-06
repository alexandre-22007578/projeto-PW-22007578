from django import forms
from django.forms import ModelForm
from .models import Post
from .models import Quizz


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
    # inserção de classes CSS para formatação de cada campo do formulário
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'descrição da tarefa...'}),
            'prioridade': forms.NumberInput(attrs={'class': 'form-control', 'max': 3, 'min': 1}),
        }


    # texto a exibir junto à janela de inserção
        labels = {
            'titulo': 'Título',
            'concluido': 'Concluída',
        }


    # texto auxiliar a um determinado campo do formulário
        help_texts = {
            'prioridade': 'prioridade: baixa=1, media=2, alta=3',
        }


class QuizzForm(ModelForm):
    class Meta:
        model = Quizz
        fields = '__all__'
    # inserção de classes CSS para formatação de cada campo do formulário
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'introduza o seu nome ...'}),
        }


    # texto a exibir junto à janela de inserção
        labels = {
            'nome': 'Qual o seu nome',
            'pergunta1': 'Qual a ferramente responsável pela estilização de uma página web',
            'pergunta2': 'Em que ano foi criado o django',
            'pergunta3': 'Qual a linguagem de programação utilizada no django',
            'pergunta4': 'Que outra linguagem de programação é usada na criação de uma web pag',
        }


