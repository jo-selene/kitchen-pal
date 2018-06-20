from django.test import TestCase
from .models import User

from datetime import date

# Create your tests here.

class UserModelTestCases(TestCase):

	def createUser(self):
		''' Test the creation of a User.'''
		self.user_ID = 1234
		self.first_name = "Billy"
		self.last_name = "Joe"
		self.user_name = "Billy.Joe"

		self.user1234 = User(user_ID=self.user_ID, first_name=self.first_name, last_name=self.last_name, 
			user_name=self.user_name, account_creation_date =date.today(),account_last_modified=date.today())
