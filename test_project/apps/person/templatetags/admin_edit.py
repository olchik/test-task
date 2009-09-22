"""
Tag that returns edit anchor in admin app
"""
from django import template

register = template.Library()


@register.inclusion_tag('templatetags/admin_include.html', takes_context=True)
def edit_list(context, content_object):
    """
    Represents tag that returns edit anchor in admin app
    """
    return {'app_label': content_object._meta.app_label,
            'module_name': content_object._meta.module_name,
            'id': content_object.id,
            'caption': "Admin edit", }
