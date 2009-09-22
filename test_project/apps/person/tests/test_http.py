"""
Tests suite for person app
"""
import sys
import os

sys.path.insert(0, 'c:\\test-task')
sys.path.insert(0, 'C:\\test-task\\test_project')
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from django.conf import settings
from tddspry.django import HttpTestCase
from tddspry.django.helpers import PASSWORD, USERNAME


class TestHomePage(HttpTestCase):
    """
    Tests for home page
    """

    def test_homepage(self):
        """
        Tests home page. It should display current user personal info.
        """
        self.go200('/')
        self.url('/login/')

        user = self.helper('create_user')
        profile = user.get_profile()
        profile.bio = "Bio"
        profile.birthday = "1987-12-08"
        profile.save()

        self.login(USERNAME, PASSWORD)
        self.go200('/')
        self.find(user.username)
        self.find(user.first_name)
        self.find(user.last_name)
        self.find(user.email)
        self.find(user.get_profile().bio)
        self.find(user.get_profile().birthday)


class TestAuthorization(HttpTestCase):
    """
    Authorization tests
    """

    def test_login(self):
        """
        Test for login
        """
        self.go200('/')
        self.url('/login/')

        user = self.helper('create_user')
        self.login(USERNAME, PASSWORD)
        self.go200('/')
        self.find(user.username)

    def test_logout(self):
        """
        Test for logout
        """
        user = self.helper('create_user')
        self.login(USERNAME, PASSWORD)

        self.go200('/')
        self.find(user.username)

        self.logout()
        self.go200('/')
        self.url('/login/')
