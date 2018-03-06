from django.db import models
from django.urls import reverse
# Create your models here.


class Restaurant(models.Model):
    JAPANESE = 'JP'
    CHINESE = 'CN'
    KOREAN = 'KO'
    EUROPEAN = 'EU'
    PLACE_TYPE_CHOICES = (
        (JAPANESE, '일식'),
        (CHINESE, '중식'),
        (KOREAN, '한식'),
        (EUROPEAN, '유럽식'),
    )
    lon = models.FloatField()
    lat = models.FloatField()
    zoom = models.PositiveSmallIntegerField(default=15)
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=2, choices=PLACE_TYPE_CHOICES, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('geofood:restaurantdetail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title