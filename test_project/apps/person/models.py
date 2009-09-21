from django.db import models
from django.contrib.auth.models import User


class Contacts(models.Model):
    """
    Person's contact info
    """
    address = models.CharField(u"Address", max_length=255, null=True, 
blank=True)
    phone = models.CharField(u"Phone", max_length=10, null=True, blank=True)

    def __unicode__(self):
        return u"%s, %s" % (self.address, self.phone)

class Profile(models.Model):
    """
    User's profile
    """
    user = models.ForeignKey(User, unique=True, related_name="profile")
    bio = models.TextField(u"Bio", null=True, blank=True)
    fk_contacts = models.ForeignKey(Contacts)
    birthday = models.DateField(u"Birthday", null=True, blank=True)

    def __unicode__(self):
        return u"User %s profile" % self.user

    class Meta:
        verbose_name = u"Profile"
        verbose_name_plural = u"Profiles"
