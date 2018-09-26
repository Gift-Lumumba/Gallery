from django.test import TestCase
from .models import Location,Category,Image

# Create your tests here.
class LocationTestClass(TestCase):
  
    # Set up method
    def setUp(self):
        self.nairobi= Location(name = 'Nairobi', description ='This is the capital city of Kenya')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.nairobi,Location))

    # Testing Save Method
    def test_save_method(self):
        self.nairobi.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

class CategoryTestClass(TestCase):
  
    # Set up method
    def setUp(self):
        self.nature= Category(name = 'Nature', description ='This is a test for Category class')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.nature,Category))

    # Testing Save Method
    def test_save_method(self):
        self.nature.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

