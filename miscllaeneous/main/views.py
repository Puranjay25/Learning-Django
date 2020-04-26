from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
	if request.method=='POST':
		form=UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('main:index')
	form=UserCreationForm()
	return render(request,"index.html",{"form":form})

def next(request):
	return render(request,"nextpage.html")

def nextpagenumber(request,pagenumber):
	if pagenumber==1:
		return render(request,"pagenumber1.html")

	elif pagenumber==2:
		return render(request,"pagenumber2.html")

	elif pagenumber==3:
		return render(request,"pagenumber3.html")