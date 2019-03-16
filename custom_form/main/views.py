from django.shortcuts import render
from django.http import HttpResponse
from .models import user
# Create your views here.
def index(request):
	return render(request,"index.html")

def signup(request):
	if request.method=="POST":
		first_name=request.POST.get("first_name")
		last_name=request.POST.get("last_name")
		username=request.POST.get("username")
		email=request.POST.get("email")
		password=request.POST.get("password")
		confirm_password=request.POST.get("confirm_password")

		t=user.objects.get_or_create(first_name=first_name,last_name=last_name,username=username,email=email,password=password,confirm_password=confirm_password)
		t[0].save()

	return render(request,"signup.html")