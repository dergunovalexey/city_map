from django.contrib import admin
from pit.models import Pit


@admin.register(Pit)
class PitAdmin(admin.ModelAdmin):
    fieldsets = (
        ('координаты', {'fields': ('latitude', 'longitude')}),
        ('параметры', {'fields': ('number_of_jolting', 'speed')}),
        ('дата и время', {'fields': ('created_at',)}),
    )
    readonly_fields = ('created_at', )
    list_filter = ('created_at', )
    search_fields = ('latitude', 'longitude', 'number_of_jolting', 'speed')
