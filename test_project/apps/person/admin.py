from django.contrib import admin
from models import Profile, Contacts


class ContactsAdmin(admin.ModelAdmin):
    list_display = ("id", "address", "phone", )

admin.site.register(Contacts, ContactsAdmin)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ("bio", "fk_contacts", "birthday", "user", )

admin.site.register(Profile, ProfileAdmin)
