from django.shortcuts import render
from .models import images
from django.http import HttpResponse 
# Create your views here.

def home(request):
	if request.method =="POST":
		name = request.POST['name']
		img = request.FILES['img']
		images.objects.create(name=name,image=img)
		return HttpResponse('uploaded')
	return render(request,'sub_app/home.html')

def view(request):
	context = {'image':images.objects.all()}
	return render(request,'sub_app/viewimage.html',context)