from django.db import models


class Viewer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(blank=True)

    @property
    def full_name(self):
        return f"{self.last_name} {self.first_name}"

    def __str__(self):
        return self.full_name

class Actor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    @property
    def full_name(self):
        return f"{self.last_name} {self.first_name}"

    def __str__(self):
        return self.full_name

class Country(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Hall(models.Model):
    name = models.CharField(max_length=100)
    rows = models.PositiveIntegerField()
    seats_per_row = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    contrives = models.ManyToManyField(Country)
    actors = models.ManyToManyField(Actor)
    genre = models.CharField(max_length=100)
    duration = models.PositiveIntegerField()  # in minutes
    poster = models.ImageField(upload_to='posters/', blank=True, null=True)

    def __str__(self):
        return self.title

class Session(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    duration = models.DurationField()

    def __str__(self):
        return f"{self.movie.title} - {self.start_time}"

class Seat(models.Model):
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    row = models.PositiveIntegerField()
    number = models.PositiveIntegerField()

    def __str__(self):
        return f"Ряд {self.row}, місце {self.number} (зал {self.hall})"

class Booking(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    viewer = models.ForeignKey(Viewer, on_delete=models.CASCADE)
    seats = models.ManyToManyField(Seat)
    created_at = models.DateTimeField(auto_now_add=True)