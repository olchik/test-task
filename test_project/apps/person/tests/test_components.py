"""
Tests suite for person app
"""
import sys
import os

sys.path.insert(0, 'c:\\test-task')
sys.path.insert(0, 'C:\\test-task\\test_project')
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from django import template
from django.contrib.auth.models import User
from django.conf import settings
from django.core.urlresolvers import reverse
from tddspry import NoseTestCase
from tddspry.django.helpers import PASSWORD, USERNAME
from person.templatetags.admin_edit import edit_list


def raise_exception():
    token = template.Token(template.TOKEN_BLOCK, u'edit_list user 2')
    edit_list(None, token)


class TestComponents(NoseTestCase):
    """
    Tests for some components of person app
    """

    def test_admin_edit(self):
        """
        Tests template tag that returns url in admin app
        """
        token = template.Token(template.TOKEN_BLOCK, u'edit_list user')
        node = edit_list(None, token)
        user, is_new = User.objects.get_or_create(id=1)
        context = {"user": user, }
        self.assert_equal(node.render(context), \
u'<a href="/admin/auth/user/1/">Admin edit</a>')

    def test_admin_edit_with_2_args(self):
        """
        Tests template tag that returns url in admin app.
        Passing wrong count of arguments
        """
        self.assert_raises(template.TemplateSyntaxError, raise_exception)
