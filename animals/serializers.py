from rest_framework import serializers
from rest_framework.exceptions import APIException

from animals.models import AnimalSex, Animal

from groups.models import Group
from traits.models import Trait

from groups.serializers import GroupSerializer
from traits.serializers import TraitSerializer

from math import log
class ValidationFieldError(APIException):
    status_code = 422
    default_value = 'unprocessable_entity'
    
class AnimalSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)    
    name = serializers.CharField(max_length = 50)
    age = serializers.IntegerField()
    weight = serializers.FloatField()
    sex = serializers.ChoiceField(choices = AnimalSex.choices, default = AnimalSex.DEFAULT)
    
    traits = TraitSerializer(many = True)
    group = GroupSerializer()

    age_in_human_years = serializers.SerializerMethodField('get_convert_dog_age_to_human_years')
    def get_convert_dog_age_to_human_years(self, animal: dict) -> float:
        return Animal.convert_dog_age_to_human_years(animal)

    def create(self, validated_data: dict) -> dict:
        trait_data = validated_data.pop('traits')
        group_data = validated_data.pop('group')

        group, _ = Group.objects.get_or_create(**group_data)
        animal = Animal.objects.create(**validated_data, group = group)
        
        for trait in trait_data:
            trait, _ = Trait.objects.get_or_create(**trait)
            animal.traits.add(trait)
        
        return animal
    
    def update(self, instance: Animal, validated_data: dict) -> dict:
        exclude = ('traits', 'group', 'sex')
        errors = {}
        
        for field, value in validated_data.items():
            if field in exclude:
                errors.update({field: f'You can not update {field} property.'})
                continue
                            
            setattr(instance, field, value)
            
        if errors:
            raise ValidationFieldError(errors)
            
        instance.save()
        
        return instance