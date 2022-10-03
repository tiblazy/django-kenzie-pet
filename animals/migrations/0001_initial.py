# Generated by Django 4.1.1 on 2022-10-03 22:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('traits', '0001_initial'),
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('age', models.IntegerField()),
                ('weigth', models.FloatField()),
                ('sex', models.CharField(max_length=15)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='animal', to='groups.group')),
                ('traits', models.ManyToManyField(related_name='animal', to='traits.trait')),
            ],
        ),
    ]