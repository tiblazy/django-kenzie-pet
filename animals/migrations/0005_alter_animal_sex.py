# Generated by Django 4.1.1 on 2022-10-05 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0004_alter_animal_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='sex',
            field=models.CharField(default='Não Informado', max_length=15),
        ),
    ]
