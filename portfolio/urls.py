from django.urls import path
from . import views

app_name = 'portfolio'
name = 'home'
urlpatterns = [
    path('', views.home_page_view, name='home'),
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

    path('', views.home_page_view),

]
