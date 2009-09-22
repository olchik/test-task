"""
Tests suite for statistics app
"""
import sys
import os

sys.path.insert(0, 'c:\\test-task')
sys.path.insert(0, 'C:\\test-task\\test_project')
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from django.conf import settings
from tddspry.django import DatabaseTestCase
from statistics.models import SQLLog

DEFAULT_URL = "www.google.com"
RAW_SQL = "Select * from something"
EXECUTION_TIME = 1


class TestSQLLogModel(DatabaseTestCase):
    """
    Tests for SQLLog model
    """

    def test_create(self):
        self.assert_create(SQLLog, url=DEFAULT_URL,
raw_sql=DEFAULT_URL, execution_time=EXECUTION_TIME)

    def test_delete(self):
        request_info = self.assert_create(SQLLog, url=DEFAULT_URL,
raw_sql=DEFAULT_URL, execution_time=EXECUTION_TIME)
        self.assert_delete(request_info)

    def test_read(self):
        self.assert_create(SQLLog, url=DEFAULT_URL,
raw_sql=DEFAULT_URL, execution_time=EXECUTION_TIME)
        self.assert_read(SQLLog, url=DEFAULT_URL,
raw_sql=DEFAULT_URL, execution_time=EXECUTION_TIME)

    def test_update(self):
        request_info = self.assert_create(SQLLog, url=DEFAULT_URL,
raw_sql=DEFAULT_URL, execution_time=EXECUTION_TIME)
        self.assert_update(request_info, raw_sql="Some sql")

    def test_unicode(self):
        request_info = self.assert_create(SQLLog, url=DEFAULT_URL,
raw_sql=DEFAULT_URL, execution_time=EXECUTION_TIME)
        self.assert_equal(unicode(request_info),
                          u"Request info for %s" % DEFAULT_URL)
