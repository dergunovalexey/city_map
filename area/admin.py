from django.contrib import admin
from area.models import MicroArea


@admin.register(MicroArea)
class MicroAreaAdmin(admin.ModelAdmin):
    fieldsets = (
        ('1я точка квадрата', {'fields': ('latitude_left', 'longitude_left')}),
        ('2я точка квадрата',
         {'fields': ('latitude_right', 'longitude_right')}),
        ('состояние', {'fields': ('level',)}),
    )
