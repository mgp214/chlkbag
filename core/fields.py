import re

from django.db import models

def parse_routeGrade(grade_string):
	p1 = re.compile('(?P<yds_class>[12345])\.(?P<yds_decimal>\d{1,2})(?P<yds_letter>[abdc]{0,1})(?P<modifier>[-+]{0,1}) (?P<yds_protection>(?:G|PG(?:13){0,1}|R|X)) (?P<yds_length>(?:IV|I{1,3}|VI{0,2}))$')
	match = p1.match(grade_string)
	result = RouteGrade(
		yds_class=match.group(1),
		yds_decimal=match.group(2),
		yds_letter = match.group(3),
		yds_modifier = match.group(4),
		yds_protection = match.group(5),
		yds_length = match.group(6)
	)
	'''	result.yds_class = match.group(1)
	result.yds_decimal = match.group(2)
	result.yds_letter = match.group(3)
	result.yds_modifier = match.group(4)
	result.yds_protection = match.group(5)
	result.yds_length = match.group(6)'''
	return result

class RouteGrade(object):	
	def __init__(self, **kwargs):
		self.yds_class = 5
		self.yds_decimal = None
		self.yds_letter = None
		self.yds_modifier = None
		self.yds_length = 'I'
		self.yds_protection = 'G'
		if 'yds_class' in kwargs:
			self.yds_class = kwargs['yds_class']
		if 'yds_decimal' in kwargs:
			self.yds_decimal = kwargs['yds_decimal']
		if 'yds_letter' in kwargs:
			self.yds_letter = kwargs['yds_letter']
		if 'yds_modifier' in kwargs:
			self.yds_modifier = kwargs['yds_modifier']
		if 'yds_length' in kwargs:
			self.yds_length = kwargs['yds_length']
		if 'yds_protection' in kwargs:
			self.yds_protection = kwargs['yds_protection']
	def __str__(self):
		stringified_value = str(self.yds_class)
		if self.yds_decimal != None:
			stringified_value = stringified_value + '.' + str(self.yds_decimal) + self.yds_letter + self.yds_modifier
		stringified_value = stringified_value + ' ' + self.yds_protection + ' ' + self.yds_length 		
		return stringified_value
	def get_grade_from_string(value):
		return parse_routeGrade(value)
		
class RouteGradeField(models.Field):

	description = "A roped climb difficulty grade."
	
	def __init__(self, *args, **kwargs):
		kwargs['max_length'] = 25
		super(RouteGradeField, self).__init__(*args, **kwargs)

	def	deconstruct(self):
		name, path, args, kwargs = super(RouteGradeField, self).deconstruct()
		del kwargs["max_length"]
		return name, path, args, kwargs

	def from_db_value(self, value, expression, connection, context):
		if value is None:
			return value
		return parse_routeGrade(value)

	def to_python(self, value):
		if isinstance(value, RouteGrade):
			return value

		if value is None:
			return value

		return parse_routeGrade(value)

		
