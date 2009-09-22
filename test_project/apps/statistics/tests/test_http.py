import sys
import os

sys.path.insert(0, 'c:\\test-task')
sys.path.insert(0, 'C:\\test-task\\test_project')
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from tddspry.django import HttpTestCase
from statistics.models import SQLLog


class TestSQLLogMiddleware(HttpTestCase):
    """
    Tests for SQLLog middleware
    """

    def test_sqllog_middleware(self):
        """
        Tests SQLLog middleware
        """
        logs_count = SQLLog.objects.all().count()
        self.go200('/login/')
        self.url('/login/')
        new_logs_count = SQLLog.objects.all().count()
        self.assert_equals(logs_count, new_logs_count - 1)
