from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
def homePageview(request):
	return HttpResponse('HelloWorld')