from django.conf import settings
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from person.forms import ProfileEditForm
from django.http import HttpResponseRedirect


@login_required
def process_root_request(request, template_name='home.html'):
    """
    Displays user's information
    """
    context = RequestContext(request, {})
    return render_to_response(template_name, context)


@login_required
def edit_profile(request, template_name='edit_profile.html'):
    """
    Edit profile page
    """
    user = request.user
    if request.method == 'POST':
        form = ProfileEditForm(data=request.POST, instance=user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = ProfileEditForm(instance=user)
    context = RequestContext(request, {"form": form,
'profile': user.get_profile(), })
    return render_to_response(template_name, context)
