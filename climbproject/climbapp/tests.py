from django.test import TestCase

from .models import ClimbModel
 # Create your tests here.
class ClimbTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='bob', email='bob@mail.com', password='passwordbob')
        ClimbModel.objects.create(climb="lion", author=self.user)
        ClimbModel.objects.create(climb="cat", author=self.user)
        
     def test_Climb_to_string(self):
        lion = ClimbModel.objects.get(climb="lion")
        cat = ClimbModel.objects.get(climb="cat")
        self.assertEqual(str(lion), 'lion')
        self.assertEqual(str(cat), 'cat')
        self.assertEqual(lion.author, self.user)
