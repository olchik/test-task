from django.db import models


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
