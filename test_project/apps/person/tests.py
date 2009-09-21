"""
Tests suite for person app
"""
import sys
import os

sys.path.insert(0, 'c:\\test-task')
sys.path.insert(0, 'C:\\test-task\\test_project')
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from django.conf import settings
from tddspry.django import HttpTestCase, DatabaseTestCase
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from person.models import Contacts, Profile

DEFAULT_ADDRESS = "Lviv, Zelena str 130"
DEFAULT_PHONE = "911"


class TestContactsModel(DatabaseTestCase):
    """
    Tests for contacts model
    """
    def test_create(self):
        self.assert_create(Contacts, address=DEFAULT_ADDRESS, phone=DEFAULT_PHONE)

    def test_delete(self):
        contact = self.assert_create(Contacts, address=DEFAULT_ADDRESS, 
                                     phone=DEFAULT_PHONE)
        self.assert_delete(contact)

    def test_read(self):
        self.assert_create(Contacts, address=DEFAULT_ADDRESS, phone=DEFAULT_PHONE)
        self.assert_read(Contacts, address=DEFAULT_ADDRESS, phone=DEFAULT_PHONE)

    def test_update(self):
        contact = self.assert_create(Contacts, address=DEFAULT_ADDRESS, 
                                     phone=DEFAULT_PHONE)
        self.assert_update(contact, address="Kharkov, L.Slobody str")

    def test_unicode(self):
        contact = self.assert_create(Contacts, address=DEFAULT_ADDRESS, 
                                     phone=DEFAULT_PHONE)
        self.assert_equal(unicode(contact), 
                          u"%s, %s"  % (DEFAULT_ADDRESS, DEFAULT_PHONE))


class TestProfileModel(DatabaseTestCase):
    """
    Tests for profile model
    """
    def setup(self):
        super(TestProfileModel, self).setup()
        self.user = self.helper('create_user')
        self.contacts = Contacts(address=DEFAULT_ADDRESS, phone=DEFAULT_PHONE)
        self.contacts.save()

    def test_create(self):
        self.assert_create(Profile, user=self.user, fk_contacts=self.contacts)

    def test_delete(self):
        profile = self.assert_create(Profile, user=self.user, 
                                     fk_contacts=self.contacts)
        self.assert_delete(profile)

    def test_read(self):
        self.assert_create(Profile, user=self.user, fk_contacts=self.contacts)
        self.assert_read(Profile, user=self.user, fk_contacts=self.contacts)

    def test_update(self):
        profile = self.assert_create(Profile, user=self.user, 
                                     fk_contacts=self.contacts)
        self.assert_update(profile, bio="Info")

    def test_unicode(self):
        profile = self.assert_create(Profile, user=self.user, 
                                     fk_contacts=self.contacts)
        self.assert_equal(unicode(profile), 
                          u"User %s profile" % self.user)
                


class TestHomePage(HttpTestCase):
    """
    Tests for home page
    """
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
