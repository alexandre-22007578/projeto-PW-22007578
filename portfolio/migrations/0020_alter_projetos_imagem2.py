# Generated by Django 4.0.4 on 2022-06-09 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0019_projetos_imagem2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projetos',
            name='imagem2',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]
