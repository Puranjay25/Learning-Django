from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
from .models import user
from django.core import serializers
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

		if password==confirm_password:
			t=user.objects.get_or_create(first_name=first_name,last_name=last_name,username=username,email=email,password=password,confirm_password=confirm_password)
			t[0].save()
			send_mail('Welcome!!','Welcome to The App community','your_email_id',[email],fail_silently=False)
		else:
			error="Password And Confirm Password do not match"
			return render(request,"signup.html",context={"error":error})

	return render(request,"signup.html")

def login(request):
	if request.method=="POST":
		username=request.POST.get("username")
		password=request.POST.get("password")

		t=user.objects.all()

		for t1 in t:
			if t1.username==username:
				if t1.password==password:
					request.session['username']=username
					u=request.session['username']
					return render(request,"dashboard.html",context={"u":u})
				else:
					error="Password do not match"
					return render(request,"login.html",context={"error":error})
			else:
				error="Username does not exists"
				return render(request,"login.html",context={"error":error})

	return render(request,"login.html")