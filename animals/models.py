from django.db import models


class AnimalSex(models.TextChoices):
    MALE = 'Macho'
    FEMALE = 'Femea'
    OTHER = 'Não Informado'
    
class Animal(models.Model):
    name = models.CharField(max_length=50, unique = True)
    age = models.IntegerField()
    weight = models.FloatField()
    sex = models.CharField(max_length=15)
    
    traits = models.ManyToManyField('traits.Trait', related_name = 'animal')
    group = models.ForeignKey('groups.Group', on_delete = models.CASCADE, related_name = 'animal')