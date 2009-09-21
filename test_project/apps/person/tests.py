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
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User


class TestHomePage(HttpTestCase):

    def test_homepage(self):
        self.go200('/')
        self.url('/')
        user = get_object_or_404(User, pk=1)
        self.find(user.username)
        self.find(user.first_name)
        self.find(user.last_name)
        self.find(user.email)
        self.find(user.get_profile().bio)


if __name__ == "__main__":
    import nose
    nose.run()
