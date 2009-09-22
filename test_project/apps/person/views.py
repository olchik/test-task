from django.conf import settings
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


@login_required
def process_root_request(request, template_name='home.html'):
    """
    Displays user's information
    """
    context = RequestContext(request, {})
    return render_to_response(template_name, context)
