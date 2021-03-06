# Generated by Django 4.0.4 on 2022-05-24 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Quizz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('pergunta1', models.CharField(max_length=200)),
                ('pergunta2', models.CharField(max_length=200)),
                ('pergunta3', models.CharField(max_length=200)),
                ('pergunta4', models.CharField(max_length=200)),
            ],
        ),
        migrations.RenameField(
            model_name='post',
            old_name='discrição',
            new_name='descrição',
        ),
        migrations.CreateModel(
            name='Projetos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('descrição', models.CharField(max_length=500)),
                ('git', models.CharField(max_length=200)),
                ('alunos', models.ManyToManyField(to='portfolio.pessoas')),
            ],
        ),
        migrations.CreateModel(
            name='Cadeira',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('rank', models.IntegerField()),
                ('link', models.CharField(max_length=200)),
                ('professores', models.ManyToManyField(to='portfolio.pessoas')),
                ('projetos', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='portfolio.projetos')),
            ],
        ),
    ]
