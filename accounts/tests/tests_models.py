from django.test import TestCase
from accounts.models import Profile
from model_bakery import baker


class ModelTestCase(TestCase):
    """ This class define test suite for account models """

    def setUp(self):
        """ """
        self.profiles = baker.make(Profile, _quantity=6)

    def test_model_total_count(self):
        """ Test total count """
        TOTAL_COUNT = 6
        self.assertEqual(Profile.objects.count(), TOTAL_COUNT)

    def test_model_profile_object(self):
        """  Test for single profile   """
        first_profile = self.profiles[0]
        first_profile_object = Profile.objects.first()

        self.assertEqual(first_profile, first_profile_object)

    def test_model_profile_exist_in_query(self):
        """ Test profile if exist in profiles object list """
        second_profile = self.profiles[1]
        profiles = Profile.objects.all()

        self.assertIn(second_profile, profiles)

