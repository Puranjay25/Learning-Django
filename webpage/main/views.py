from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def home(request):
	return render(request=request,template_name="home.html")

def signup(request):
	form=UserCreationForm
	return render(request,"signup.html",context={"form":form})

def wrongsignup(request,number):
	return HttpResponse("Oops!..Somethong went wrong")