from django.db import models
from django.contrib.postgres.fields import JSONField


class RoadTreck(models.Model):
    start = JSONField()
    end = JSONField()
    accselerometer_points = JSONField()
    magnetometer_points = JSONField()
