# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(request):
	return HttpResponse("This is my first app <strong>Hello World</strong>")
