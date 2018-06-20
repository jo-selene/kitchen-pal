# File Name:        User/models.py
# Creation Date:    5/19/2018
# Last Edited:      5/19/2018
# Author(s):        Jocelyne Perez
#
# Purpose:          The purpose of this file is to define the User model and its attributes.
#                   The model is meant to store data unique to each user.
#
# Notes:            If changes are made to the model, go to the root folder and migrate the changes
#                   using the command $ python manage.py makemigrations

from django.db import models

class User(models.Model):
	""" This class represents the User model """

	user_ID = models.IntegerField(unique="True",primary_key="True")
	first_name = models.CharField(max_length=25)
	last_name = models.CharField(max_length=25)
	user_name = models.CharField(max_length=25, unique="True")
	account_creation_date = models.DateField(auto_now_add="True")
	account_last_modified = models.DateField(auto_now_add="True")

	def __str__(self):
		return '{}'.format(self.user_name)



