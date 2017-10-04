from django.contrib import admin
from django.contrib.gis import admin as gis_admin
from .models import Region, Area, Route, User

admin.site.register(Region)
admin.site.register(Area, gis_admin.OSMGeoAdmin)
admin.site.register(Route)
admin.site.register(User)

