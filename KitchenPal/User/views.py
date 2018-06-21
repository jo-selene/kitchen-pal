# File Name:        User/views.py
# Creation Date:    5/19/2018
# Last Edited:      5/20/2018
# Author(s):        Jocelyne Perez
#
# Purpose:          The purpose of this file is to create a few views for the User model.
#
# Notes:            None


from django.shortcuts import render
from rest_framework import generics
from .models import User
from .serializer import UserSerializer
# Create your views here.


class CreateUserView(generics.CreateAPIView):
	""" This class defines the create (POST) behaviour of our API """

	serializer_class = UserSerializer

	def perform_create(self,serializer):
		serializer.save()
