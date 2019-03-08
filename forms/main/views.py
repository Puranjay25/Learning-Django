from django.shortcuts import render
from django.http import HttpResponse
from .models import user
from .forms import userform
# Create your views here.
def index(request):
	form=userform(request.POST)
	if request.method=="POST":
		if form.is_valid():
			form.save()
		return render(request=request,template_name="main.html")
	else:
		users=user.objects.all()
		print(users)
		return render(request=request,template_name="main.html",context={"users":users,"form":form})