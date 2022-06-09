from django.db import models


# Create your models here.


class Post(models.Model):
    titulo = models.CharField(max_length=200)
    descrição = models.CharField(max_length=500)
    prioridade = models.IntegerField(default=1)
    concluido = models.BooleanField(default=False)
    criado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo[:200]

    class Meta:
        ordering = ['-prioridade']


class Quizz(models.Model):
    nome = models.CharField(max_length=200)
    pergunta1 = models.CharField(max_length=200)
    pergunta2 = models.CharField(max_length=200)
    pergunta3 = models.CharField(max_length=200)
    pergunta4 = models.CharField(max_length=200)

    def __str__(self):
        return self.nome[:200]


class Pessoas(models.Model):
    nome = models.CharField(max_length=200)
    link = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.nome[:200]


def resolution_path(instance, filename):
    return f'users/{instance.id}/'


class Projetos(models.Model):
    nome = models.CharField(max_length=200)
    descrição = models.CharField(max_length=500)
    ano = models.IntegerField(default=0)
    git = models.CharField(max_length=200, null=True, blank=True)
    alunos = models.ManyToManyField(Pessoas)
    imagem = models.ImageField(upload_to='media/', null=True, blank=True)
    imagem2 = models.URLField(max_length=500, null=True , blank=True)

    def __str__(self):
        return self.nome[:200]


    class Meta:
        ordering = ['-imagem']


class Cadeira(models.Model):
    nome = models.CharField(max_length=200)
    ano = models.IntegerField(default=0)
    semestre = models.IntegerField(default=0)
    creditos = models.IntegerField(default=0)
    professores = models.ManyToManyField(Pessoas, related_name='cadeiras')
    rank = models.IntegerField(default=0)
    link = models.CharField(max_length=200)
    projetos = models.OneToOneField(Projetos, blank=True, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nome[:200]


class Tecnologias(models.Model):
    nome = models.CharField(max_length=200)
    acrónimo = models.CharField(max_length=5)
    ano = models.IntegerField(default=0)
    logotipo = models.ImageField(upload_to='media/', null=True, blank=True)
    descrição = models.CharField(max_length=5000)

    def __str__(self):
        return self.nome[:200]


class Tecnologias2(models.Model):
    nome = models.CharField(max_length=200)
    acrónimo = models.CharField(max_length=5)
    ano = models.IntegerField(default=0)
    logotipo = models.ImageField(upload_to='media/', null=True, blank=True)
    descrição = models.CharField(max_length=5000)

    def __str__(self):
        return self.nome[:200]


class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    numero = models.IntegerField(default=0)
    descrição = models.CharField(max_length=50000)
    link = models.CharField(max_length=2000)
    imagem = models.ImageField(upload_to='media/', null=True, blank=True)

    def __str__(self):
        return self.titulo[:200]
