# File Name:        Kitchen/models.py
# Creation Date:    4/25/2018
# Last Edited:      4/28/2018
# Author(s):        Jocelyne Perez
#
# Purpose:          The purpose of this file is to define the MyKitchen model and its attributes.
#                   The model is meant to store data unique to each user.
#                   Each row of data for this model will hold a users identification and an item ID
#                   that will reference a Food model.
#
# Notes:            If changes are made to the model, go to the root folder and migrate the changes
#                   using the command $ python manage.py makemigrations


from django.db import models
from Food.models import Food

# Create your models here.

class Kitchen(models.Model):
    """ This class represents the kitchen model """
    
    kitchen_ID = models.CharField(max_length=50,primary_key="True")
    '''user_ID = models.CharField(max_length=50,one_to_many="True")
    food_ID = models.ForeignKey('Food',on_delete=models.DONOTHING)'''
    
    def __str__(self):
        return '{}:{}'.format(self.kitchen_ID)


    
