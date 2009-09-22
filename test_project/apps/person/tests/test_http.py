"""
Tests suite for person app
"""
import sys
import os

sys.path.insert(0, 'c:\\test-task')
sys.path.insert(0, 'C:\\test-task\\test_project')
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from django.conf import settings
from django.core.urlresolvers import reverse
from tddspry.django import HttpTestCase
from tddspry.django.helpers import PASSWORD, USERNAME
from person.forms import DateWidget

NEW_FIRST_NAME = "olchik"
NEW_LAST_NAME = "ABS"
NEW_EMAIL = "email@email.com"
NEW_PHONE = "911"
NEW_ADDRESS = "Lviv, Antonovucha str."
NEW_BIRTHDAY = "1987-12-12"
NEW_BIO = "description"


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

    def test_context_processor(self):
        """
        Tests whether settings has been added to context.
        Tries to find DEFAULT_GREETING string from settings.
        """
        self.go200('/login/')
        self.url('/login/')
        self.find(settings.DEFAULT_GREETING)


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


class TestProfiles(HttpTestCase):
    """
    Profiles tests
    """

    def test_edit_profile(self):
        """
        Test of editing profile
        """
        user = self.helper('create_user')
        self.login(USERNAME, PASSWORD)
        self.go200(reverse('person.views.edit_profile'))
        self.formvalue(1, 'id_first_name', NEW_FIRST_NAME)
        self.formvalue(1, 'id_last_name', NEW_LAST_NAME)
        self.formvalue(1, 'id_email', NEW_EMAIL)
        self.formvalue(1, 'id_phone', NEW_PHONE)
        self.formvalue(1, 'id_address', NEW_ADDRESS)
        self.formvalue(1, 'id_birthday', NEW_BIRTHDAY)
        self.formvalue(1, 'id_bio', NEW_BIO)
        self.submit200()
        self.url('/')
        self.find(NEW_FIRST_NAME)
        self.find(NEW_LAST_NAME)
        self.find(NEW_EMAIL)
        self.find(NEW_PHONE)
        self.find(NEW_ADDRESS)
        self.find(NEW_BIRTHDAY)
        self.find(NEW_BIO)

    def test_invalid_email(self):
        """
        Test of editing profile. Filling invalid email.
        """
        user = self.helper('create_user')
        self.login(USERNAME, PASSWORD)
        self.go200(reverse('person.views.edit_profile'))
        self.formvalue(1, 'id_email', "email")
        self.submit200()
        self.find("Enter a valid e-mail address.")

    def test_datepicker_loadded(self):
        """
        Checks that birthday field use data picker in profile edit page
        """
        # Checks whether media can be loaded
        for css_urls in DateWidget.Media.css.values():
            for css_url in css_urls:
                self.go200(css_url)
        for js_url in DateWidget.Media.js:
            self.go200(js_url)

        # Checks whether java script that binds data picker loaded
        user = self.helper('create_user')
        self.login(USERNAME, PASSWORD)
        self.go200(reverse('person.views.edit_profile'))
        custom_js = DateWidget.JS_INIT_FORMAT_STRING % {u"name": "birthday", }
        self.find(custom_js, flat=True)
