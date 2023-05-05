from django.db import models
from django.urls import reverse

class Crop(models.Model):
    name = models.CharField(max_length=200)
    state = models.CharField(max_length=100)
    sowing_date = models.DateField()
    area = models.FloatField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('crop_detail', args=[str(self.id)])
