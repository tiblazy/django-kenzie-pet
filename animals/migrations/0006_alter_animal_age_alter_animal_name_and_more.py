# Generated by Django 4.1.1 on 2022-10-05 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0005_alter_animal_sex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='animal',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='animal',
            name='weight',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
