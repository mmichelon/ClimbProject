from django.test import TestCase

from .models import ClimbModel
 # Create your tests here.
class ClimbTestCase(TestCase):
    def setUp(self):
        ClimbModel.objects.create(climb="lion")
        ClimbModel.objects.create(climb="cat")
     def test_Climb_to_string(self):
        lion = ClimbModel.objects.get(climb="lion")
        cat = ClimbModel.objects.get(climb="cat")
        self.assertEqual(str(lion), 'lion')
        self.assertEqual(str(cat), 'cat')
