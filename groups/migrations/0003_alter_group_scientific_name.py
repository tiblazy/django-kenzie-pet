# Generated by Django 4.1.1 on 2022-10-05 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_alter_group_scientific_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='scientific_name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
