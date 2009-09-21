from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.models import User


def process_root_request(request, template_name='home.html'):
    """
    Displays 1st user's information 
    """
    user = get_object_or_404(User, pk=1)
    return render_to_response(template_name, {'user': user, })
