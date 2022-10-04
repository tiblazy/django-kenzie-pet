from rest_framework import serializers

from animals.models import AnimalSex

class AnimalSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)    
    name = serializers.CharField(max_length = 50)
    age = serializers.IntegerField()
    weight = serializers.FloatField()
    sex = serializers.ChoiceField(choices = AnimalSex.choices, default = AnimalSex.DEFAULT)