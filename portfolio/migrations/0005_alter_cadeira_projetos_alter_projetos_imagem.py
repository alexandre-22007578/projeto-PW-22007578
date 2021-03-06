# Generated by Django 4.0.4 on 2022-05-24 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_cadeira_creditos_projetos_ano_projetos_imagem_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadeira',
            name='projetos',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='portfolio.projetos'),
        ),
        migrations.AlterField(
            model_name='projetos',
            name='imagem',
            field=models.ImageField(null=True, upload_to='media/'),
        ),
    ]
