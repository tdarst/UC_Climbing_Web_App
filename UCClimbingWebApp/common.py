from django.conf import settings
from django.contrib.auth.decorators import user_passes_test
from functools import wraps
from django.shortcuts import redirect
from django.http import HttpResponse
from PIL import Image

def logout_required(redirect_to=None):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapper_view(request, *args, **kwargs):
            if request.user.is_authenticated:
                redirect_url = redirect_to if redirect_to else settings.HOME_URL
                return redirect(redirect_url)
            return view_func(request, *args, **kwargs)
        return _wrapper_view
    return decorator