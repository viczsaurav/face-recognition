from django.shortcuts import render

# Create your views here.

def train(request):
	return render(request,'webcamrecog/train.html')