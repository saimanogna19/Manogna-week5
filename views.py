from django.shortcuts import render
from django.http import HttpResponse
import json
def index(request):
	data={'Message':'Hello World, I am Sai Manogna and this is my first django project for software Architecture & Design'}
	return HttpResponse(json.dumps(data),content_type="application/json")