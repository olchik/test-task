"""
Tests for some components of statistics app
"""

import sys
import os
os.environ["DJANGO_SETTINGS_MODULE"] = "test_project.settings"

from tddspry.django import DatabaseTestCase
from statistics.management.commands.modelslog import Command
from cStringIO import StringIO
from django.db.models.loading import get_model


class TestModelsLogCommand(DatabaseTestCase):
    """
    Tests for manage command modelslog
    """

    def test_modellog(self):
        """
        Test for manage command modelslog
        """
        cmd = Command()
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        try:
            cmd.handle()
            output = sys.stdout.getvalue()
        finally:
            sys.stdout = old_stdout

        lines = output.split('\n')
        for line in lines:
            if line: # Check for blank line in the end
                items = line.split(" ")
                model_name = items[0]
                app = items[1]
                count = int(items[2])
                model = get_model(app, model_name)
                actual_count = model.objects.all().count()
                self.assert_equal(actual_count, count)
