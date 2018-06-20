# File Name:        Recipes/models.py
# Creation Date:    5/8/2018
# Last Edited:      5/8/2018
# Author(s):        Jocelyne Perez
#
# Purpose:          The purpose of this file is to write all test cases related to the 'Recipe'
#                   model.
#
# Notes:            To run test cases, go to root folder of this project and run the command
#                   $ python manage.py test

from django.db import models

class Recipe(models.Model):
    """ This class represents the Recipe model """
    recipe_ID = models.IntegerField(primary_key="True")
    name = models.CharField(max_length=50)
    instructions = models.CharField(max_length=400)
    cooking_time = models.IntegerField()
    servings = models.IntegerField()
        # objects = RecipeManager()

    def __str__(self):
        return self.name

'''class RecipeManager(models.Manager):

    def add_recipe_to_database(self, name, instructions, cooking_time, servings):
        self.recipe = Recipe(recipe_ID=123, name=name, instructions=instructions, cooking_time= cooking_time,    servings=servings)

        self.save()

'''
