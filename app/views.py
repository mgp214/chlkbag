from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponse

from .models import Route, Area, Region

class IndexView(generic.ListView):
	template_name = 'app/index.html'
	context_object_name = 'routes_nearby'
	def get_queryset(self):
		return Route.objects.all()
