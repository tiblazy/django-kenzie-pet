# from sqlite3 import IntegrityError
from django.test import TestCase
from django.db import IntegrityError

from groups.models import Group

class GroupModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.group_data = {
            'name': 'Reptile',
            'scientific_name': 'Reptilia',
        }
        
        cls.group = Group.objects.create(**cls.group_data)        
    
    def test_group_model(self) -> None:
        name_max_length = self.group._meta.get_field('name').max_length
        name_nullable = self.group._meta.get_field("name").null
        name_blankable = self.group._meta.get_field("name").blank
        name_unique = self.group._meta.get_field('name').unique

        scientific_name_max_length = self.group._meta.get_field('scientific_name').max_length
        scientific_name_nullable = self.group._meta.get_field("scientific_name").null
        scientific_name_blankable = self.group._meta.get_field("scientific_name").blank
        scientific_name_unique = self.group._meta.get_field('scientific_name').unique

        self.assertEqual(name_max_length, 20)
        self.assertFalse(name_nullable)
        self.assertFalse(name_blankable)
        self.assertTrue(name_unique)
        
        self.assertEqual(scientific_name_max_length, 50)
        self.assertFalse(scientific_name_nullable)
        self.assertFalse(scientific_name_blankable)
        self.assertTrue(scientific_name_unique)
        
    def test_if_raise_error_when_group_already_exists(self):
        with self.assertRaises(IntegrityError):
            group = Group.objects.create(**self.group_data)

            self.group = group
            self.group.save()
            