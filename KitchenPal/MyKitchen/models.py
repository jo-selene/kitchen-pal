# File Name:        MyKitchen/models.py
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

class MyKitchen(models.Model):
    """ This class represents the kitchen model """

    user = models.CharField(max_length=50)
    itemID = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.self.user

    
