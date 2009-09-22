"""
Tests suite for person app
"""
import os
os.environ["DJANGO_SETTINGS_MODULE"] = "test_project.settings"

from tddspry.django.helpers import PASSWORD, USERNAME
from tddspry.django import HttpTestCase


class TestComponents(HttpTestCase):
    """
    Tests for some components of person app
    """

    def test_admin_edit(self):
        """
        Tests template tag that returns url in admin app
        """
        user = self.helper('create_user')
        self.login(USERNAME, PASSWORD)
        self.find(u'<a href="/admin/auth/user/%d/">Admin edit</a>' % user.id)
