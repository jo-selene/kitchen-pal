# File Name:        User/views.py
# Creation Date:    5/19/2018
# Last Edited:      5/20/2018
# Author(s):        Jocelyne Perez
#
# Purpose:          The purpose of this file is to create a few views for the User model.
#
# Notes:            None


from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from rest_framework import generics
from .models import User
from .serializer import UserSerializer
# Create your views here.


def index(request):
	# In a sanbox phase, next step is to remove the current code in index and replace it with the creation/log-in of users
	all_users = User.objects.all()
	template = loader.get_template('User/index.html')
	context = {
		'all_users' : all_users,

	}
	return HttpResponse(template.render(context,request))
	
class CreateUserView(generics.CreateAPIView):
	""" This class defines the create (POST) behaviour of our API """

	serializer_class = UserSerializer

	def perform_create(self,serializer):
		serializer.save()

