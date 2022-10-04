from rest_framework import serializers

from animals.models import AnimalSex, Animal

from groups.models import Group
from traits.models import Trait

from groups.serializers import GroupSerializer
from traits.serializers import TraitSerializer
class AnimalSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)    
    name = serializers.CharField(max_length = 50)
    age = serializers.IntegerField()
    weight = serializers.FloatField()
    sex = serializers.ChoiceField(choices = AnimalSex.choices, default = AnimalSex.DEFAULT)
    
    traits = TraitSerializer(many = True)
    group = GroupSerializer()

    def create(self, validated_data: dict):
        trait_data = validated_data.pop('traits')
        group_data = validated_data.pop('group')

        group, _ = Group.objects.get_or_create(**group_data)
        animal = Animal.objects.create(**validated_data, group = group)
        
        for trait in trait_data:
            trait, _ = Trait.objects.get_or_create(**trait)
            animal.traits.add(trait)
        
        return animal