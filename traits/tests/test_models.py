from django.test import TestCase
from django.db import IntegrityError

from traits.models import Trait

class TraitModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.trait_data = {
            'name': 'Furious',
        }
        
        cls.trait = Trait.objects.create(**cls.trait_data)
    
    def test_trait_model(self) -> None:
        max_length = self.trait._meta.get_field('name').max_length
        nullable = self.trait._meta.get_field("name").null
        blankable = self.trait._meta.get_field("name").blank
        unique = self.trait._meta.get_field('name').unique
        
        self.assertEqual(max_length, 20)
        self.assertFalse(nullable)
        self.assertFalse(blankable)
        self.assertTrue(unique)
        
    def test_if_raise_error_when_trait_already_exists(self):
        with self.assertRaises(IntegrityError):
            trait = Trait.objects.create(**self.trait_data)
        
            self.trait = trait
            self.trait.save()