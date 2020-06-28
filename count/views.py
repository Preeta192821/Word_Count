
from django.shortcuts import render


def home(request):
	return render(request,'home.html')


def about(request):
	return render(request,'about.html')


def feedback(request):
	return render(request,'feedback.html')

def word(request):
	return render(request,'word.html')


def count(request):
	text = request.GET['word']
	count=len(text.split())
	return render(request,'count.html',{'count':count,'text':text})
















# Create your views here.
