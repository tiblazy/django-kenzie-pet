from sqlite3 import IntegrityError
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

    def test_animal_model(self) -> None:
        animal = Animal.objects.get(name = 'Barrigada')
        
        name_max_length = self.animal._meta.get_field('name').max_length
        name_nullable = self.animal._meta.get_field('name').null
        name_blankable = self.animal._meta.get_field('name').blank
        name_unique = self.animal._meta.get_field('name').unique

        sex_max_length = self.animal._meta.get_field('sex').max_length
        sex_nullable = self.animal._meta.get_field('sex').null
        sex_blankable = self.animal._meta.get_field('sex').blank
        sex_unique = self.animal._meta.get_field('sex').unique
        
        self.assertIsInstance(animal, Animal)
        self.assertEqual(animal, self.animal)

        self.assertEqual(name_max_length, 50)
        self.assertFalse(name_nullable)
        self.assertFalse(name_blankable)
        self.assertFalse(name_unique)
        
        self.assertEqual(sex_max_length, 15)
        self.assertFalse(sex_nullable)
        self.assertFalse(sex_blankable)
        self.assertFalse(sex_unique)
        
    def test_animal_can_be_attached_to_multiple_traits(self):
        for trait in self.traits:
            self.animal.traits.add(trait)
            
        self.assertEquals(len(self.traits), self.animal.traits.count())
        
        for trait in self.traits:
            self.assertIn(self.animal, trait.animals.all())
    
    def test_convert_dog_age_to_human_years(self):
        age = Animal.objects.get(age = 13)
        
        self.assertEqual(age.convert_dog_age_to_human_years(), 72.03918971938458)