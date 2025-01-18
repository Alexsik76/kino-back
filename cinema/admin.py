from django.contrib import admin
from cinema.models import Viewer, Hall, Movie, Session, Seat, Booking


admin.site.register([Viewer, Hall, Movie, Session, Seat, Booking])
