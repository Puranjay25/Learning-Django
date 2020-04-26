from django.shortcuts import render, redirect
from django.http import HttpResponse
from main.models import CustomUser

# Create your views here.
def index(request):
	return render(request, "index.html")

def signup(request):
	if request.method == "POST":
		username = request.POST["username"]
		email = request.POST["email"]
		password = request.POST["password"]
		cpassword = request.POST["cpassword"]
		CustomUser.objects.create_user(username=username,email=email,password=cpassword)
		
		return redirect('main:index')
	return render(request, "login.html")


