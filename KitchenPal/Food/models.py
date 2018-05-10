# File Name:        Food/models.py
# Creation Date:    4/25/2018
# Last Edited:      4/28/2018
# Author(s):        Jocelyne Perez
#
# Purpose:          The purpose of this file is to define the Food model and its attributes.
#                   The model is meant to store data that will model food objects.
#
# Notes:            If changes are made to the model, go to the root folder and migrate the changes
#                   using the command $ python manage.py makemigrations

from django.db import models


class Food(models.Model):
    """ This class will represent Food objects """
    food_ID = models.IntegerField(primary_key="True")
    name = models.CharField(max_length=50,unique=True)
    type = models.CharField(max_length=50)
    longevity = models.IntegerField(default=0)
    longevityType = models.CharField(max_length=50)
    storageType = models.CharField(max_length=50)
    storageTips = models.CharField(max_length=255)

    def __str__(self):
        """ Return a human readable representation of the model/object """
        return "{}".format(self.name)
