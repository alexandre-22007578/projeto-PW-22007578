# Generated by Django 4.0.4 on 2022-05-24 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_alter_projetos_ano'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projetos',
            name='ano',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='projetos',
            name='git',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
