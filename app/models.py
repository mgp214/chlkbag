from django.db import models
from django.contrib.gis.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
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
	region = models.ForeignKey('Region', on_delete=models.CASCADE, default=None, null=True)
	area = models.MultiPolygonField(
		'Area',
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
	yds_class = models.IntegerField(
		'YDS class',
		default=5,
		validators=[
			MaxValueValidator(5),
			MinValueValidator(1)
		]
	)
	yds_decimal = models.IntegerField(
		'YDS 5th class decimal',
		null=True,
		blank=True,
		default=None,
		validators=[
			MinValueValidator(0)
		]
	)
	yds_letter = models.CharField(
		'YDS difficulty letter',
		max_length=1,
		choices=(
			('a', 'a'),
			('b', 'b'),
			('c', 'c'),
			('d', 'd')
		),
		null=True,
		blank=True,
		default=None
	)
	yds_modifier = models.CharField(
		'YDS difficulty modifier',
		max_length=1,
		choices=(
			('+', 'plus'),
			('-', 'minus')
		),
		null=True,
		blank=True,
		default=None
	)
		
	yds_protection = models.CharField(
		'YDS protection rating',
		max_length=4,
		choices=(
			('G', 'G'),
			('PG', 'PG'),
			('PG13', 'PG13'),
			('R', 'R'),
			('X', 'X')
		),
		default='G'
	)
	yds_length = models.CharField(
		'YDS length grade',
		max_length=3,
		choices=(
			('I', 'I: 1-2 hours'),
			('II', 'II: Less than a half-day'),
			('III', 'III: Half day'),
			('IV', 'IV: Full day'),
			('V', 'V: 2-3 days'),
			('VI', 'VI: 4-6 days'),
			('VII', 'VII: 1 week or longer')
		),
		default='I'
	)
	def __str__(self):
		return self.name
