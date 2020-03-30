from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    likes = models.IntegerField(default=0)
    unlikes = models.IntegerField(default=0)
    release_year = models.DateField()
    actors = models.ManyToManyField('Actor', related_name='actor_movies')
    directors = models.ManyToManyField(
        'Director', related_name='director_movies')

    def __str__(self):
        return self.title


class Director(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Actor(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    def __str__(self):
        return self.commented_by
