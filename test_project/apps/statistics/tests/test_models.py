"""
Tests suite for statistics app
"""
import os
os.environ["DJANGO_SETTINGS_MODULE"] = "test_project.settings"

from tddspry.django import DatabaseTestCase
from statistics.models import SQLLog

# Default values for SQLLog
DEFAULT_URL = "www.google.com"
RAW_SQL = "Select * from something"
EXECUTION_TIME = 1

# Default values for ModelLog
DEFAULT_MODEL = "model"
OPERATION_TYPE = 1
MODEL_PK = 1


class TestSQLLogModel(DatabaseTestCase):
    """
    Tests for SQLLog model
    """

    def test_create(self):
        """
        Tests SQLLog creating
        """
        self.assert_create(SQLLog, url=DEFAULT_URL,
raw_sql=DEFAULT_URL, execution_time=EXECUTION_TIME)

    def test_delete(self):
        """
        Tests SQLLog deleting
        """
        request_info = self.assert_create(SQLLog, url=DEFAULT_URL,
raw_sql=DEFAULT_URL, execution_time=EXECUTION_TIME)
        self.assert_delete(request_info)

    def test_read(self):
        """
        Tests SQLLog reading
        """
        self.assert_create(SQLLog, url=DEFAULT_URL,
raw_sql=DEFAULT_URL, execution_time=EXECUTION_TIME)
        self.assert_read(SQLLog, url=DEFAULT_URL,
raw_sql=DEFAULT_URL, execution_time=EXECUTION_TIME)

    def test_update(self):
        """
        Tests SQLLog updating
        """
        request_info = self.assert_create(SQLLog, url=DEFAULT_URL,
raw_sql=DEFAULT_URL, execution_time=EXECUTION_TIME)
        self.assert_update(request_info, raw_sql="Some sql")

    def test_unicode(self):
        """
        Tests for unicode representation of SQLLog
        """
        request_info = self.assert_create(SQLLog, url=DEFAULT_URL,
raw_sql=DEFAULT_URL, execution_time=EXECUTION_TIME)
        self.assert_equal(unicode(request_info),
                          u"Request info for %s" % DEFAULT_URL)


class ModelLog(DatabaseTestCase):
    """
    Tests for ModelLog model
    """

    def test_create(self):
        """
        Tests ModelLog creating
        """
        self.assert_create(ModelLog, model=DEFAULT_MODEL,
model_pk=MODEL_PK, operation_type=OPERATION_TYPE)

    def test_delete(self):
        """
        Tests ModelLog deleting
        """
        model_log = self.assert_create(ModelLog, model=DEFAULT_MODEL,
model_pk=MODEL_PK, operation_type=OPERATION_TYPE)
        self.assert_delete(model_log)

    def test_read(self):
        """
        Tests ModelLog reading
        """
        self.assert_create(ModelLog, model=DEFAULT_MODEL,
model_pk=MODEL_PK, operation_type=OPERATION_TYPE)
        self.assert_read(ModelLog, model=DEFAULT_MODEL,
model_pk=MODEL_PK, operation_type=OPERATION_TYPE)

    def test_update(self):
        """
        Tests ModelLog updating
        """
        model_log = self.assert_create(ModelLog, model=DEFAULT_MODEL,
model_pk=MODEL_PK, operation_type=OPERATION_TYPE)
        self.assert_update(model_log, model_id=2)

    def test_unicode(self):
        """
        Tests for unicode representation of ModelLog
        """
        model_log = self.assert_create(ModelLog, model=DEFAULT_MODEL,
model_pk=MODEL_PK, operation_type=OPERATION_TYPE)
        self.assert_equal(unicode(model_log),
                          u"Info about model %s" % DEFAULT_MODEL)

    def test_login_user(self):
        """
        Checks model log when
        creating/updating/deleting user
        """
        user = self.helper("create_user")
        self.assert_read(ModelLog, model=user.__name__,
model_pk=user.pk, operation_type=1)

        user.first_name = "olchik"
        user.save()
        self.assert_read(ModelLog, model=user.__name__,
model_pk=user.pk, operation_type=2)

        user.delete()
        self.assert_read(ModelLog, model=user.__name__,
model_pk=user.pk, operation_type=3)
