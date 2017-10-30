# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import LoginForm
from django.http import HttpResponse
# Create your views here.


def index(request):
    form = LoginForm()
    return render(request, 'login.html', {'form': form})