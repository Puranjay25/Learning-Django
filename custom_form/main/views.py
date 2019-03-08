from django.shortcuts import render
from django.http import HttpResponse
from .models import test
# Create your views here.
def index(request):
	if request.method=="POST":
		t=request.POST.get("user")
		temp=test.objects.get_or_create(text=t)
		temp[0].save()
	return render(request,"index.html")