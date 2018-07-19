from django.contrib import admin
from trackrecorder.models import RoadTreck


@admin.register(RoadTreck)
class RoadTrackAdmin(admin.ModelAdmin):
    pass
