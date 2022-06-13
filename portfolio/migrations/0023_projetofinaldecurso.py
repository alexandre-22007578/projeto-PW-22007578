# Generated by Django 4.0.4 on 2022-06-13 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0022_noticia_imagem2'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjetoFinalDeCurso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.IntegerField(default=0)),
                ('titulo', models.CharField(max_length=2000)),
                ('resumo', models.CharField(max_length=2000)),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('imagem2', models.URLField(blank=True, max_length=500, null=True)),
                ('link', models.CharField(max_length=200)),
                ('autores', models.ManyToManyField(related_name='autores', to='portfolio.pessoas')),
                ('orientadores', models.ManyToManyField(related_name='orientadores', to='portfolio.pessoas')),
            ],
        ),
    ]