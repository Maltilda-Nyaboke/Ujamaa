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

    def test_save_method(self):
        self.neighborhood.create_neighborhood()
        neighborhoods = Neighborhood.objects.all()
        self.assertTrue(len(neighborhoods) > 0)

    def test_delete_method(self):
        self.neighborhood.create_neighborhood()
        self.neighborhood.delete()
        neighborhoods = Neighborhood.objects.all()
        self.assertTrue(len(neighborhoods) == 0)



class LocationTestClass(TestCase):
    def setUp(self):
        self.location = Location(name='Test Location')

    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))

    def test_save_method(self):
        self.location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    def test_delete_method(self):
        self.location.save_location()
        self.location.delete()
        locations = Location.objects.all()
        self.assertTrue(len(locations) == 0)        

