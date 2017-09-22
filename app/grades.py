import re

from django.db import models

def parse_routeGrade(grade_string):
	p1 = re.compile('(?P<yds_class>[12345])\.(?P<yds_decimal>\d{1,2})(?P<yds_letter>[abdc]{0,1})(?P<modifier>[-+]{0,1}) (?P<yds_protection>(?:G|PG(?:13){0,1}|R|X)) (?P<yds_length>(?:IV|I{1,3}|VI{0,2}))$')
	match = p1.match(grade_string)
	result = RouteGrade()
	result.yds_class = match.group(1)
	result.yds_decimal = match.group(2)
	result.yds_letter = match.group(3)
	result.yds_modifier = match.group(4)
	result.yds_protection = match.group(5)
	result.yds_length = match.group(6)
	return result

class RouteGrade(object):
	yds_class = 5
	yds_decimal = 0
	yds_letter = None
	yds_modifier = None
	yds_length = 'I'
	yds_protection = 'G'

class RouteGradeField(models.Field):

	description = "A roped climb difficulty grade."
	
	def __init__(self, *args, **kwargs):
		kwargs['max_length'] = 100
		super(RouteGradeField, self).__init__(*args, **kwargs)
	
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

		
