from django.db import models
from django.contrib.gis.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser
from django.conf import settings
'''from core.fields import RouteGrade'''

class Region(models.Model):
	name = models.CharField('Name', max_length=50)
	description = models.TextField('Description')
	getting_there = models.TextField('How to get there')
	contents = models.PolygonField(
		'Area',
		null=True,
		blank=True,
		default=None,
		geography=True)
	def __str__(self):
		return self.name
	
class Area(models.Model):
	name = models.CharField('Name', max_length=50)
	description = models.TextField('Description')
	getting_there = models.TextField('How to get there')
	region = models.ForeignKey(Region, on_delete=models.CASCADE, default=None, null=True)
	polygon = models.PolygonField(
		'Polygon',
		null=True,
		blank=True,
		default=None,
		geography=True)
	def __str__(self):
		return self.name

class Route(models.Model):
	name = models.CharField('Name', max_length=50)
	description = models.TextField('Description')
	getting_there = models.TextField('How to get there')
	
	first_ascent_names = models.CharField('First Ascender', max_length=50)
	first_ascent_date = models.DateField('First Ascent Date')
	area = models.ForeignKey(Area, on_delete=models.CASCADE)
	coordinates = models.PointField(
		'Coordinates',
		null=True,
		blank=True,
		default=None,
		geography=True)
	grade = models.CharField('YDS grade', max_length=25, null=True, blank=True, default=None)
	def get_grade_obj(self):
		return RouteGrade.get_grade_from_string(grade)

	def __str__(self):
		return self.name

class User(AbstractUser):
	first_name = models.CharField(max_length=15, blank=True)
	last_name = models.CharField(max_length=15, blank=True)
	home_town = models.CharField(max_length=25, blank=True)
	bio = models.TextField(max_length=500, blank=True)
	email = models.EmailField()
	birth_date = models.DateField(null=True, blank=True)
	home_region = models.ForeignKey(Region,null=True, blank=True)
	favorite_areas = models.ManyToManyField(Area, blank=True)
	favorite_climbs = models.ManyToManyField(Route, blank=True)
	def __str__(self):
		return self.username
'''	favorite_problems = models.ManyToManyField(Problem, blank=True)'''
class RouteEntry(models.Model):	
	ascent_date = models.DateField('Ascent Date')
	creation_date = models.DateField('Date Created')
	modified_date = models.DateField('Date Last Modufied', 
		blank=True, null=True, default=None
	)
	route = models.ForeignKey(Route, on_delete=models.CASCADE)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	
