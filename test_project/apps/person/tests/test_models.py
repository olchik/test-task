"""
Tests suite for person app
"""
import os
os.environ["DJANGO_SETTINGS_MODULE"] = "test_project.settings"

from tddspry.django import DatabaseTestCase
from person.models import Contacts, Profile

DEFAULT_ADDRESS = "Lviv, Zelena str 130"
DEFAULT_PHONE = "911"


class TestContactsModel(DatabaseTestCase):
    """
    Tests for contacts model
    """

    def test_create(self):
        """
        Tests Contacts creating
        """
        self.assert_create(Contacts, address=DEFAULT_ADDRESS,
phone=DEFAULT_PHONE)

    def test_delete(self):
        """
        Tests Contacts deleting
        """
        contact = self.assert_create(Contacts, address=DEFAULT_ADDRESS,
                                     phone=DEFAULT_PHONE)
        self.assert_delete(contact)

    def test_read(self):
        """
        Tests Contacts reading
        """
        self.assert_create(Contacts, address=DEFAULT_ADDRESS,
phone=DEFAULT_PHONE)
        self.assert_read(Contacts, address=DEFAULT_ADDRESS,
phone=DEFAULT_PHONE)

    def test_update(self):
        """
        Tests Contacts updating
        """
        contact = self.assert_create(Contacts, address=DEFAULT_ADDRESS,
                                     phone=DEFAULT_PHONE)
        self.assert_update(contact, address="Kharkov, L.Slobody str")

    def test_unicode(self):
        """
        Tests for string representation of Contacts
        """
        contact = self.assert_create(Contacts, address=DEFAULT_ADDRESS,
                                     phone=DEFAULT_PHONE)
        self.assert_equal(unicode(contact),
                          u"%s, %s" % (DEFAULT_ADDRESS, DEFAULT_PHONE))


class TestProfileModel(DatabaseTestCase):
    """
    Tests for profile model
    """

    def setup(self):
        """
        Pre-test setup method
        """
        super(TestProfileModel, self).setup()
        self.user = self.helper('create_user')
        self.profile = self.user.get_profile()

    def test_create(self):
        """
        Tests Profile creating
        """
        self.assert_count(Profile, 2)

    def test_delete(self):
        """
        Tests Profile deleting
        """
        self.assert_delete(self.profile)

    def test_read(self):
        """
        Tests Profile reading
        """
        self.assert_read(Profile, user=self.user)

    def test_update(self):
        """
        Tests Profile updating
        """
        self.assert_update(self.profile, bio="Info")

    def test_unicode(self):
        """
        Tests for string representation of Profile
        """
        self.assert_equal(unicode(self.profile),
                          u"User %s profile" % self.user)
