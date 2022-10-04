from django.test import TestCase
from groups.models import Group

class GroupModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.group_data = {
            'name': 'Reptile',
            'scientific_name': 'Reptilia',
        }
        
        cls.group = Group.objects.create(**cls.group_data)
        
    def test_name_max_length(self) -> None:
        max_length = self.group._meta.get_field('name').max_length
        
        self.assertEqual(max_length, 20)
        
    def test_name_unique(self) -> None:
        unique = self.group._meta.get_field('name').unique
        
        self.assertTrue(unique)
    
    def test_name_can_be_null_or_blank(self):
        nullable = self.group._meta.get_field("name").null
        blankable = self.group._meta.get_field("name").blank

        self.assertFalse(nullable)
        self.assertFalse(blankable)
    
    def test_scientific_name_max_length(self) -> None:
        max_length = self.group._meta.get_field('scientific_name').max_length
        
        self.assertEqual(max_length, 50)
    
    def test_scientific_name_unique(self) -> None:
        unique = self.group._meta.get_field('scientific_name').unique
        
        self.assertTrue(unique)
        
    def test_scientific_name_can_be_null_or_blank(self):
        nullable = self.group._meta.get_field("scientific_name").null
        blankable = self.group._meta.get_field("scientific_name").blank

        self.assertFalse(nullable)
        self.assertFalse(blankable)
