from django.http import HttpResponse
from django.shortcuts import redirect, render 
from functools import wraps

from rest_framework.response import Response

def allowed_users(allowed_roles=()):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper_func(request, *args, **kwargs):
            if request.user.groups.filter(name__in=allowed_roles).exists():
                return view_func(request, *args, **kwargs)
            else:
                return Response("you haven't access here ")
        return wrapper_func
    return decorator