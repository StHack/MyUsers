#-*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.conf import settings

def logout_required(view):
    def f(request, *args, **kwargs):
        if request.user.is_anonymous():
            return view(request, *args, **kwargs)
        return HttpResponseRedirect("/")
    return f