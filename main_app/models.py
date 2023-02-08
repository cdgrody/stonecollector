from django.db import models
from django.urls import reverse

# Create your models here.
class Stone(models.Model):
    name = models.CharField(max_length=100)
    # numberOptions = [0,1,2,3,4,5,6,7,8,9,10]
    # colorOptions = ['red', 'purple', 'yellow', 'orange', 'blue', 'green', 'black', 'white', 'tansparent'] make these tuples
    numberOfAppearances = models.PositiveSmallIntegerField()
    color = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f'The {self.name} has made {self.numberOfAppearances} appearances and is {self.color}.'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'stone_id': self.id})

