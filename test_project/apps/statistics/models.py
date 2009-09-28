from django.db import models
from django.db.models.loading import get_models
from django.db.models.signals import post_save, post_delete


class SQLLog(models.Model):
    """
    Stores information about db requests
    """
    url = models.URLField("Url", max_length=50, null=True, blank=True)
    raw_sql = models.CharField(u"Raw sql", max_length=255, null=True,
blank=True)
    execution_time = models.IntegerField(u"Execution time", default=0)

    def __unicode__(self):
        return u"Request info for %s" % self.url

    class Meta:
        verbose_name = u"Database request info"
        verbose_name_plural = u"Database requests info"


OPERATION_TYPE = (
    (1, u'Create'),
    (2, u'Update'),
    (3, u'Delete'),
)


class ModelLog(models.Model):
    """
    Stores information about creating/updating/deleting models
    """
    model = models.CharField(u"Model name", max_length=255, null=False)
    model_pk = models.CharField(u"Primary key", null=True, max_length=255)
    operation_type = models.IntegerField(u"Operation type", default=1,
choices=OPERATION_TYPE)
    date = models.DateField("Date", auto_now=True)

    def __unicode__(self):
        return u"ModelLog of %s model" % self.model

    class Meta:
        verbose_name = u"Model manipulation info"
        verbose_name_plural = u"Model manipulations info"


def log_delete(sender, **kwargs):
    """
    Saves info about model objects deleting
    """
    instance = kwargs['instance']
    log_model(sender, 3, instance)


def log_update(sender, created, **kwargs):
    """
    Saves info about model objects updating or creating
    """
    operation_type = 1 if created else 2
    instance = kwargs['instance']
    log_model(sender, operation_type, instance)


def log_model(sender, operation_type, instance):
    """
    Saves info about model objects manipulations to database
    """
    log = ModelLog(model = sender.__name__, model_pk = instance.pk,
operation_type=operation_type)
    log.save()


def bind_logging():
    """
    Binds signals for models that saves info about
    model objects manipulations to database
    """
    models_list = get_models()
    for model in models_list:
        if model.__name__ != "ModelLog" and model.__name__ != "SQLLog" \
and model.__name__ != "LogEntry":
            post_save.connect(log_update, sender=model)
            post_delete.connect(log_delete, sender=model)

bind_logging()
