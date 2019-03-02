from django.shortcuts import render
from django.http import HttpResponse
from .models import user
from .forms import userform
# Create your views here.
def index(request):
	if request.method=="POST":
		form=userform(request.POST)
		if form.is_valid():
			form.save()
			return render(request=request,template_name="main.html")

	return render(request=request,template_name="main.html")