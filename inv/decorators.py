from collections import namedtuple
from django.http import HttpResponse, request
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect ('home')
        else:
            return view_func(request,*args,**kwargs)
    return wrapper_func


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request,*args,**kwargs):
            group=None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request,*args,**kwargs)
            else:
                return redirect('restricted')
        return wrapper_func
    return decorator


def admin_only(view_func):
    def wrapper_function(request,*args,**kwargs):
        group=None
        if request.user.groups.exists():
            group=request.user.groups.all()[0].name

        if group=='engineer':
            return redirect('engineer_dashboard')

        if group=='teamleader' or group=='staff':
            return redirect('teamleader_dashboard')

        else:
            return view_func(request,*args,**kwargs)

    return wrapper_function
