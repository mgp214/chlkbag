from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from core.models import Route, Area, Region

#class IndexView(generic.ListView):
#	template_name = 'map/index.html'
#	context_object_name = 'routes_nearby'
#	def get_queryset(self):
#		return Route.objects.all()
class IndexView(View):
	def get(self, request):
		context = {
			'nearby_routes': Route.objects.all(),
			'nearby_areas': Area.objects.all(),
		}
		return render(request,'map/index.html',context)
