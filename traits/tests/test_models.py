from django.test import TestCase
from traits.models import Trait

class TraitModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.trait_data = {
            'name': 'Furious',
        }
        
        cls.trait = Trait.objects.create(**cls.trait_data)
    
    def test_name_max_length(self) -> None:
        max_length = self.trait._meta.get_field('name').max_length
        
        self.assertEqual(max_length, 20)
        
    def test_name_unique(self) -> None:
        unique = self.trait._meta.get_field('name').unique
        
        self.assertTrue(unique)
        
    def test_name_can_be_null_or_blank(self) -> None:
        nullable = self.trait._meta.get_field("name").null
        blankable = self.trait._meta.get_field("name").blank

        self.assertFalse(nullable)
        self.assertFalse(blankable)