from django.test import TestCase
from animals.models import Animal
from groups.models import Group
from traits.models import Trait

class AnimalModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.group_data = {
            'name': 'Mammal',
            'scientific_name': 'Mammalia',
        }
        
        cls.group = Group.objects.create(**cls.group_data)
        
        cls.traits_data = {
            'name': 'Furious',
        }
        
        cls.traits_data_second = {
            'name': 'Nameless',
        }
        
        cls.animal_data = {
            'name': 'Barrigada',
            'age': 13,
            'weight': 23.3,
            'sex': 'Não Informado',
            'group': cls.group
            }
        
        cls.traits = [Trait.objects.create(**cls.traits_data) for _ in range(1)]
        cls.animal = Animal.objects.create(**cls.animal_data)

    def test_animal_can_be_attached_to_multiple_traits(self):
        for trait in self.traits:
            self.animal.traits.add(trait)
            
        self.assertEquals(len(self.traits), self.animal.traits.count())
        
        for trait in self.traits:
            self.assertIn(self.animal, trait.animals.all())
            
    def test_animals_age(self):
        age = Animal.objects.get(age = 13)
        
        self.assertEqual(age.convert_dog_age_to_human_years(), 72.03918971938458)