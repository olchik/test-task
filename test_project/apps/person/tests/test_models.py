"""
Tests suite for person app
"""
import sys
import os

sys.path.insert(0, 'c:\\test-task')
sys.path.insert(0, 'C:\\test-task\\test_project')
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from django.conf import settings
from tddspry.django import DatabaseTestCase
from person.models import Contacts, Profile

DEFAULT_ADDRESS = "Lviv, Zelena str 130"
DEFAULT_PHONE = "911"


class TestContactsModel(DatabaseTestCase):
    """
    Tests for contacts model
    """

    def test_create(self):
        self.assert_create(Contacts, address=DEFAULT_ADDRESS,
phone=DEFAULT_PHONE)

    def test_delete(self):
        contact = self.assert_create(Contacts, address=DEFAULT_ADDRESS,
                                     phone=DEFAULT_PHONE)
        self.assert_delete(contact)

    def test_read(self):
        self.assert_create(Contacts, address=DEFAULT_ADDRESS,
phone=DEFAULT_PHONE)
        self.assert_read(Contacts, address=DEFAULT_ADDRESS,
phone=DEFAULT_PHONE)

    def test_update(self):
        contact = self.assert_create(Contacts, address=DEFAULT_ADDRESS,
                                     phone=DEFAULT_PHONE)
        self.assert_update(contact, address="Kharkov, L.Slobody str")

    def test_unicode(self):
        contact = self.assert_create(Contacts, address=DEFAULT_ADDRESS,
                                     phone=DEFAULT_PHONE)
        self.assert_equal(unicode(contact),
                          u"%s, %s" % (DEFAULT_ADDRESS, DEFAULT_PHONE))


class TestProfileModel(DatabaseTestCase):
    """
    Tests for profile model
    """

    def setup(self):
        super(TestProfileModel, self).setup()
        self.user = self.helper('create_user')
        self.profile = self.user.get_profile()

    def test_create(self):
        self.assert_count(Profile, 2)

    def test_delete(self):
        self.assert_delete(self.profile)

    def test_read(self):
        self.assert_read(Profile, user=self.user)

    def test_update(self):
        self.assert_update(self.profile, bio="Info")

    def test_unicode(self):
        self.assert_equal(unicode(self.profile),
                          u"User %s profile" % self.user)
