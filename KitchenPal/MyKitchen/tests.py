f

from django.test import TestCase
from .models import MyKitchen
from Food.models import Food


# Create your tests here.

class MyKitchenModelTestCase(TestCase):
    """ This class defines the test suite for the MyKitchen model """

    def setUp(self):
        """ Test the creation of a users kitchen. This will mean all the food items that the
            user currently has in their home."""
        
        self.user1 = "Kenny"
        self.itemID1 = 'Banana'

        self.kennysKitchen = MyKitchen(user=self.user1,itemID=self.itemID1)
        
        self.user2 = "Jocelyne"
        self.itemID2 = 'Apples'
    
        self.jocelynesKitchen = MyKitchen(user=self.user2,itemID=self.itemID2)
    
        self.user3 = "Sally"
    
        self.sallysKitchen = MyKitchen(user=self.user3,itemID=self.itemID2)
    
    def testKitchenCanBeAddedToDB(self):
        old_count = MyKitchen.objects.count()
        self.kennysKitchen.save()
        new_count = MyKitchen.objects.count()
        self.assertNotEqual(old_count,new_count)

    def testKennysKitchenHasABanana(self):
        self.assertEqual(self.kennysKitchen.itemID,'Banana')

    def testJocelynesKitchenHasApples(self):
        self.assertEqual(self.jocelynesKitchen.itemID,'Apples')

    def testKennyAndJocelynesKitchenNotTheSame(self):
        self.assertNotEqual(self.kennysKitchen,self.jocelynesKitchen)

    def testJocelynesAndSallyHaveApples(self):
        self.kennysKitchen.save()
        self.jocelynesKitchen.save()
        self.sallysKitchen.save()

        users_with_apples = MyKitchen.objects.filter(itemID='Apples')
        self.assertEqual(list(users_with_apples),[self.jocelynesKitchen,self.sallysKitchen])

    def testStrMethodWorks(self):
        self.jocelynesKitchen.save()
        user_string = MyKitchen.objects.get(user='Jocelyne')
        print(user_string)

#  def testAllExistingUsers(self):
#       users =

   


