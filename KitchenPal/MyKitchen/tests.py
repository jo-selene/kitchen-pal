# File Name:        MyKitchen/tests.py
# Creation Date:    4/25/2018
# Last Edited:      4/28/2018
# Author(s):        Jocelyne Perez
#
# Purpose:          The purpose of this file is to write all test cases related to the 'MyKitchen'
#                   model.
#
# Notes:            To run test cases, go to root folder of this project and run the command
#                   $ python manage.py test

from django.test import TestCase
from .models import MyKitchen
from Food.models import Food


# Create your tests here.

class MyKitchenModelTestCase(TestCase):
    """ This class defines the test suite for the MyKitchen model """

    def setUp(self):
        """ Test the creation of a users kitchen. This will mean all the food items that the
            user currently has in their home."""
        
        self.user = "Kenny"
        self.itemID = 'Banana'

        self.kennysKitchen = MyKitchen(user=self.user,itemID=self.itemID)

   


