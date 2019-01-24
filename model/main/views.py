  # -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import first
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return render(request=request,template_name="home.html",context={"first":first.objects.all})
