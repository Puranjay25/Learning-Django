from django.shortcuts import render
from django.http import HttpResponse, request
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
# Create your views here.
def index(request):
	return render(request, "index.html")

def login(request):
	if request.method=="POST":
		username=request.POST.get("username")
		password=request.POST.get("password")
		try:
			user = authenticate(username=username, password=password)
			if user is not None:
				print("=================")
				auth_login(request, user)
				return HttpResponse("logged in")
			else:
				print("YYYYYYYYYYYYY")
		except Exception as e:
			raise e
	return render(request, "login.html")

def signup(request):
	if request.method=="POST":
		username=request.POST.get("username")
		password=request.POST.get("password")
		print(password)
		try:
			User.objects.create_user(username=username,password=password)
		except Exception as e:
			raise e
	return render(request, "signup.html")