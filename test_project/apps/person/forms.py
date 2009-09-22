from django import forms
from person.models import Contacts
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from django.template.loader import get_template, Context


class DateWidget(forms.widgets.Input):
    """
    Selecting date in calendar widget
    """

    class Media:
        css = {'all': ('/static/datePicker.css', ), }
        js = ('/static/date.js',
              '/static/jquery.datePicker.js', )

    def render(self, name, value, attrs=None):
        output = super(DateWidget, self).render(name, value, attrs)
        template = get_template("widgets/init_calendar.html")
        context = Context({"name": name, })
        init_script = template.render(context)
        output = output + init_script
        return mark_safe(output)


class ProfileEditForm(forms.ModelForm):
    """
    Represents form for editing profile
    """
    phone = forms.CharField(label=u'Phone', required=False)
    address = forms.CharField(label=u'Address', required=False)
    birthday = forms.DateField(required=False, widget=DateWidget)
    bio = forms.CharField(required=False, widget=forms.Textarea())

    def __init__(self, *args, **kwargs):
        super(ProfileEditForm, self).__init__(*args, **kwargs)
        if kwargs.has_key("instance"):
            user = kwargs["instance"]
            profile = user.get_profile()
            contacts = profile.fk_contacts
            self.fields["birthday"].initial = profile.birthday
            self.fields["bio"].initial = profile.bio
            self.fields["phone"].initial = contacts.phone
            self.fields["address"].initial = contacts.address

    def save(self, *args, **kwargs):
        super(ProfileEditForm, self).save(*args, **kwargs)
        user = self.instance

        profile = user.get_profile()
        profile.birthday = self.cleaned_data['birthday']
        profile.bio = self.cleaned_data['bio']
        profile.save()

        contacts = profile.fk_contacts
        contacts.phone = self.cleaned_data['phone']
        contacts.address = self.cleaned_data['address']
        contacts.save()

        return self.instance

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', )
