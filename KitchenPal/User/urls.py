# File Name:        User/urls.py
# Creation Date:    5/27/2018
# Last Edited:      5/27/2018
# Author(s):        Jocelyne Perez
#
# Purpose:          The purpose of this file is to create url's for the User model views.
#
# Notes:            None

from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateUserView, index

urlpatterns = {
    url('createuser$', CreateUserView.as_view(),name='create'),
    url('$', index, name='index')
   # url('user/(?P<pk>[0-9]+)/$', DetailsView.as_view(),name='details')
}

urlpatterns = format_suffix_patterns(urlpatterns)
