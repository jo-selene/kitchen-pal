from django.test import TestCase
from .models import MyKitchen, Food


# Create your tests here.

class MyKitchenModelTestCase(TestCase):
    """ This class defines the test suite for the MyKitchen model """

    def setUp(self):
        """ Test the creation of a users kitchen. This will mean all the food items that the
            user currently has in their home."""
        
        self.bananas = Food(1,"Fruit",1,"Week","Fridge","Keep in fridge before they get brown spots")
        self.chicken = Food(2,"Poultry",3,"Months","Freezer","Keep each chicken breast in its own ziplock bag and freeze")
        self.items = [self.bananas,self.chicken]
        self.ID = "User ID"
        self.kitchen = MyKitchen(ID=self.ID, Items=self.items)
        


