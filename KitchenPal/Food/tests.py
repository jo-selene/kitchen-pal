from django.test import TestCase
from .models import Food

# Create your tests here.

class FoodModelTestCase(TestCase):
    """ This class defines the test suite for the Food model """
    
    def setUp(self):
        """ This method tests to see whether or not an instance of the Food model can
            be created successfully or not. """
        
        self.ID = 1
        self.type = "Type"
        self.longevity = 2
        self.longevityType = "Weeks"
        self.storageType = "Fridge"
        self.storageTips = "Store in a ziplock bag and puncture a few holes in the bag"
        
        self.Food = Food(ID = self.ID, type = self.type, longevity = self.longevity,
                         longevityType = self.longevityType, storageType = self.storageType,
                         storageTips = self.storageTips)
    
    def testFoodModelCanBeAddedToDatabase(self):
        """ This method tests to see whether or not a new Food item can be added to the
            database """
        
        old_count = Food.objects.count()
        self.Food.save()
        new_count = Food.object.count()
        self.assertNotEqual(old_count,new_count)


