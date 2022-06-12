from django.urls import path
from . import views

app_name = 'portfolio'
name = 'home'
urlpatterns = [
    path('home', views.home_page_view, name='home'),
    path('competencias', views.competencias, name='competencias'),
    path('formacao', views.formacao, name='formacao'),
    path('projetos', views.projetos, name='projetos'),
    path('quizz', views.quizzPage, name='quizz'),
    path('blog', views.blog, name='blog'),
    path('about', views.about, name='about'),
    path('nova', views.nova_post_view, name='nova'),
    path('edita/<int:Post_id>', views.edita_post_view, name='edita'),
    path('apaga/<int:Post_id>', views.apaga_post_view, name='apaga'),
    path('login', views.loginSite, name='login'),
    path('logout', views.logoutSite, name='logout'),
    path('web', views.web, name='web'),
    path('api', views.APIs, name='api'),
    path('projetoFinalDeCurso', views.projetoFinalDeCurso, name='projetoFinalDeCurso'),

    path('', views.home_page_view),

]
