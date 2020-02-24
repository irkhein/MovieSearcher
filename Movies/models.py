from django.db import models
from django.urls import reverse


# genres
class Genre(models.Model):
    # id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=256)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


# persons
class Person(models.Model):
    # id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=256)
    date_of_birth = models.DateField()
    rate = models.IntegerField(default=0)
    # person_picture = models.ImageField()
    person_picture = models.FileField()
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    def rate(self):
        rate = round(
            self.like / (self.like + self.dislike) * 10
        ) if (self.like + self.dislike) > 0 else 0
        return range(0, rate)


# movies
class Movie(models.Model):
    # id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=256)
    description = models.TextField(max_length=1024)
    year = models.DateField()
    # movie_picture = models.ImageField()
    movie_picture = models.FileField()
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
    director = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    trailer_url = models.CharField(max_length=1024, null=True)

    def get_absolute_url(self):
        return reverse('Movies:movie', kwargs={'pk': self.pk})

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    def rate(self):
        rate = round(
            self.like / (self.like + self.dislike) * 10
        ) if (self.like + self.dislike) > 0 else 0
        return range(0, rate)


# roles
class Role(models.Model):
    # id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=256)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


# casting (Person <=> Movie)
class Casting(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return "{0}: {1}".format(self.movie, self.person)
