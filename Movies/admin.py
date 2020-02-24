from django.contrib import admin
from .models import (Person, Movie, Role, Genre, Casting)


admin.site.register(Person)
admin.site.register(Movie)
admin.site.register(Role)
admin.site.register(Genre)
admin.site.register(Casting)
