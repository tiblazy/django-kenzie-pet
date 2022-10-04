# Generated by Django 4.1.1 on 2022-10-03 22:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('traits', '0001_initial'),
        ('groups', '0001_initial'),
        ('animals', '0002_rename_weigth_animal_weight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='animals', to='groups.group'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='traits',
            field=models.ManyToManyField(related_name='animals', to='traits.trait'),
        ),
    ]