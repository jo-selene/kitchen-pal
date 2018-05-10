# File Name:        Food/tests.py
# Creation Date:    4/25/2018
# Last Edited:      4/28/2018
# Author(s):        Jocelyne Perez
#
# Purpose:          The purpose of this file is to write all test cases related to the 'Food'
#                   model.
#
# Notes:            To run test cases, go to root folder of this project and run the command
#                   $ python manage.py test


from django.test import TestCase
from .models import Food


class FoodModelTestCase(TestCase):
    """ This class defines the test suite for the Food model """

    def setUp(self):
        """ This method tests to see whether or not an instance of the Food model can
            be created successfully or not. """
        
        self.food_ID = 1234
        self.name = "Cilantro"
        self.type = "Type"
        self.longevity = 2
        self.longevityType = "Weeks"
        self.storageType = "Fridge"
        self.storageTips = "Store in a ziplock bag and puncture a few holes in the bag"
        
        
        
        self.cilantro = Food(food_ID=self.food_ID, name= self.name, type = self.type, longevity =  self.longevity,longevityType = self.longevityType, storageType = self.storageType, storageTips = self.storageTips)
    
    def testFoodModelCanBeAddedToDatabase(self):
        """ This method tests to see whether or not a new Food item can be added to the
            database """
        
        old_count = Food.objects.count()
        self.cilantro.save()
        new_count = Food.objects.count()
        self.assertNotEqual(old_count,new_count)

    def testStrMethodWorks(self):
        self.cilantro.save()
        food_string = Food.objects.get(name="Cilantro")
        print(food_string)



