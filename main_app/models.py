from django.db import models
from django.urls import reverse

STONE_COLORS = (('R', 'Red'), ('P', 'Purple'), ('Y', 'Yellow'), ('O', 'Orange'), ('B', 'Blue'), ('G', 'Green'),)
IS_HERO = ((True, 'Yes'), (False, 'No'),)
MOVIE_TYPE = ((True, 'Ensemble'), (False, 'Solo'),)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    is_ensemble = models.BooleanField( 'Ensemble or Solo Film', choices=MOVIE_TYPE, default=True)
    release_date = models.DateField('Release Year')

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('movies_detail', kwargs={'pk': self.id})

    class Meta:
        ordering = ['-release_date']


# Create your models here.
class Stone(models.Model):
    name = models.CharField(max_length=100)
    numberOfAppearances = models.PositiveSmallIntegerField(default=0)
    description = models.TextField()
    movies = models.ManyToManyField(Movie)
    color = models.CharField(
        max_length=100, 
        choices=STONE_COLORS,
        default=STONE_COLORS[0][1]
    )

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'stone_id': self.id})


class Weilder(models.Model):
    character = models.CharField(max_length=100)
    is_hero = models.BooleanField(choices=IS_HERO)
    phase_of_use = models.PositiveSmallIntegerField()
    stone = models.ForeignKey(Stone, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.character}'

    class Meta:
        ordering = ['-phase_of_use', 'character', 'is_hero']