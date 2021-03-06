from django.db import models
from django.contrib.auth.models import User
from simple_history.models import HistoricalRecords


class Location(models.Model):
    latitude = models.DecimalField(db_index=True, decimal_places=4, max_digits=7)
    longitude = models.DecimalField(db_index=True, decimal_places=4, max_digits=8)
    name = models.CharField(max_length=64)
    is_free = models.BooleanField(default=True)
    rating = models.FloatField(default=0.0)
    user = models.ForeignKey(User)
    male = models.BooleanField(default=True)
    female = models.BooleanField(default=True)
    flags = models.ManyToManyField(User, related_name='flagged_locations', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    is_anonymous = models.BooleanField(default=True)
    rating_count = models.IntegerField(default=0)
    _history_ = HistoricalRecords()

    def __str__(self):
        return self.name
