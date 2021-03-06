# Generated by Django 4.0.4 on 2022-05-21 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('discrição', models.CharField(max_length=500)),
                ('prioridade', models.IntegerField(default=1)),
                ('concluido', models.BooleanField(default=False)),
                ('criado', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
