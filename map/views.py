from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from core.models import Route, Area, Region

class IndexView(generic.ListView):
	template_name = 'map/index.html'
	context_object_name = 'routes_nearby'
	def get_queryset(self):
		return Route.objects.all()
