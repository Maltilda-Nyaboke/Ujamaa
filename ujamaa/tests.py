from django.test import TestCase
from .models import *
from django.contrib.auth.models import User


# Create your tests here.


class NeighborhoodTestClass(TestCase):
    def setUp(self):
        self.location = Location(name='Kilimani')
        self.location.save_location()
        self.admin = User.objects.create_superuser(
            username='maltilda',
            password='Password'
        )
        self.neighborhood = Neighborhood(
            name='victory court', location=self.location, occupants_count=120, admin_id=self.admin.id)
    
    def test_instance(self):
        self.assertTrue(isinstance(self.neighborhood, Neighborhood))


