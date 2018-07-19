from django.db import models
from django.contrib.postgres.fields import JSONField


class RoadTreck(models.Model):
    start = JSONField()
    end = JSONField()
    accselerometer_points = JSONField()
    magnetometer_points = JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
