# File Name:        Users/serializers.py
# Creation Date:    5/19/2018
# Last Edited:      5/20/2018
# Author(s):        Jocelyne Perez
#
# Purpose:          The purpose of this file is to create a serializer to map the model instance into JSON format
#
# Notes:            None


from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    """ Serializer to map the User model instance into JSON format """

    class Meta:
        """ Meta class to map the serializers fields with the model fields """
        model = User
        fields = ('user_ID','first_name','last_name','user_name','account_creation_date','account_last_modified')
       # read_only_fields = ('date_created','date_modified')


