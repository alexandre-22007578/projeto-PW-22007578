import requests
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import PostForm
from .forms import QuizzForm
from .models import Post
from .models import Quizz
from .models import Projetos
from .models import Cadeira
from .models import Noticia
from .models import Tecnologias2

from .quizz import desenha_graficodados


def home_page_view(request):
    return render(request, 'portfolio/home.html')

def competencias(request):
    return render(request, 'portfolio/competencias.html')

def web(request):
    context = {'noticias': Noticia.objects.all(), 'tecnologias': Tecnologias2.objects.all()}
    return render(request, 'portfolio/web.html', context)

def formacao(request):
    context = {'cadeiras': Cadeira.objects.all()}
    return render(request, 'portfolio/formacao.html', context)

def projetos(request):
    context = {'projetos': Projetos.objects.all()}
    return render(request, 'portfolio/projetos.html', context)

def about(request):
    return render(request, 'portfolio/about.html')

def blog(request):
    context = {'post': Post.objects.all()}
    return render(request, 'portfolio/blog.html', context)


def quizzPage(request):
    desenha_graficodados(Quizz.objects.all())
    quizz = QuizzForm(request.POST, use_required_attribute=False)
    if quizz.is_valid():
        quizz.save()
        return HttpResponseRedirect(request.path_info)

    context = {'form': quizz}

    return render(request, 'portfolio/quizz.html', context)

def nova_post_view(request):

    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:blog'))

    context = {'form': form}

    return render(request, 'portfolio/nova.html', context)

def edita_post_view(request, Post_id):

    post = Post.objects.get(id=Post_id)
    form = PostForm(request.POST or None, instance=post)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:blog'))

    context = {'form': form, 'Post_id': Post_id}
    return render(request, 'portfolio/edita.html', context)


def apaga_post_view(request, Post_id):
    Post.objects.get(id=Post_id).delete()
    return HttpResponseRedirect(reverse('portfolio:blog'))


def loginSite(request):
    if request.method == "POST":
        nome = request.POST.get('username')
        password = request.POST.get('password')
        utilizador = authenticate(request, username=nome, password=password)

        if utilizador is not None:
            login(request, utilizador)
            context = {'post': Post.objects.all()}
            return render(request, 'portfolio/blog.html', context)
        else:
            return render(
                request, 'portfolio/login.html',
                {'message': "Dados inválidos"}
            )

    return render(request, 'portfolio/login.html')


def logoutSite(request):
    logout(request)
    return render(request, 'portfolio/login.html')



def APIs(request):
    return render(request, 'portfolio/api.html')

def projetoFinalDeCurso(request):
    return render(request, 'portfolio/projetoFinalDeCurso.html')
