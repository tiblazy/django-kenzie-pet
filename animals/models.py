from django.db import models


class AnimalSex(models.TextChoices):
    MALE = 'Macho'
    FEMALE = 'Fêmea'
    DEFAULT = 'Não Informado'
    
class Animal(models.Model):
    name = models.CharField(max_length = 50)
    age = models.IntegerField() 
    weight = models.FloatField()
    sex = models.CharField(max_length = 15)
    
    traits = models.ManyToManyField('traits.Trait', related_name = 'animals')
    group = models.ForeignKey('groups.Group', on_delete = models.CASCADE, related_name = 'animals')