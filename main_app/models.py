from django.db import models
from django.urls import reverse

COLORS = (('R', 'Red'), ('P', 'Purple'), ('Y', 'Yellow'), ('O', 'Orange'), ('B', 'Blue'), ('G', 'Green'))

# Create your models here.
class Stone(models.Model):
    name = models.CharField(max_length=100)
    numberOfAppearances = models.PositiveSmallIntegerField(default=0)
    color = models.CharField(max_length=100, choices=COLORS)
    description = models.TextField()

    def __str__(self):
        return f'The {self.name} has made {self.numberOfAppearances} appearances and is {self.color}.'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'stone_id': self.id})

class Weilder(models.Model):
    character = models.CharField(max_length=100)
    is_hero = models.BooleanField()
    phase_of_use = models.PositiveSmallIntegerField()
    stone = models.ForeignKey(Stone, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.character} in Phase {self.phase_of_use}'