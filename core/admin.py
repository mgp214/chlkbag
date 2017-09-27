from django.contrib import admin

from .models import Region, Area, Route, User

admin.site.register(Region)
admin.site.register(Area)
admin.site.register(Route)
admin.site.register(User)

