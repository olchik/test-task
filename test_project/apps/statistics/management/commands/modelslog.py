from django.core.management.base import BaseCommand
from django.db.models.loading import get_models


class Command(BaseCommand):
    """
    Represents manage.py command that shows all models in the project and
    count of objects of each model
    """

    option_list = BaseCommand.option_list
    help = 'Show info about models'
    args = ''

    def handle(self, *app_labels, **options):
        models_list = get_models()
        for model in models_list:
            count = model.objects.all().count()
            print model.__name__, model._meta.app_label, count
