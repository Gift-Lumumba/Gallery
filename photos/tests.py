from django.test import TestCase
from .models import Location,Category,Image

# Create your tests here.
class LocationTestClass(TestCase):
  
    # Set up method
    def setUp(self):
        self.nairobi= Location(name = 'Nairobi', description ='This is the capital city of Kenya')
