"""
Tag that returns edit anchor in admin app
"""
from django import template

register = template.Library()


class AdminUrlNode(template.Node):
    ADMIN_URL_FORMAT = u'<a href="/admin/%s/%s/%s/">Admin edit</a>'

    def __init__(self, node):
        self.model = template.Variable(node)

    def render(self, context):
        content_object = self.model.resolve(context)
        return self.ADMIN_URL_FORMAT % (content_object._meta.app_label,
                                content_object._meta.module_name,
                                content_object.id)


@register.tag
def edit_list(parser, token):
    """
    Represents tag that returns edit anchor in admin app
    """
    try:
        tag_name, model = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError, \
"%r tag requires exactly one arguments" % token.contents.split()[0]
    return AdminUrlNode(model)
