"""
Profile models
"""
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save


class Contacts(models.Model):
    """
    Person's contact info
    """
    address = models.CharField(u"Address", max_length=255, null=True,
blank=True)
    phone = models.CharField(u"Phone", max_length=10, null=True, blank=True)

    def __unicode__(self):
        return u"%s, %s" % (self.address, self.phone)

    class Meta:
        verbose_name = u"Contact"
        verbose_name_plural = u"Contacts"


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


def create_contacts(sender, **kwargs):
    """
    Creates contacts, when profile is creating.
    """
    profile = kwargs['instance']
    if not hasattr(profile, "fk_contacts"):
        contact = Contacts()
        contact.save()
        profile.fk_contacts = contact


def create_profile(sender, **kwargs):
    """
    Creates profile, when user has been created
    """
    instance = kwargs['instance']
    profile, is_new = Profile.objects.get_or_create(user=instance)
    profile.save()


post_save.connect(create_profile, sender=User)

pre_save.connect(create_contacts, sender=Profile)
