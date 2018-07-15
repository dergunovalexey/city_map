from django.contrib import admin
from citizen.models import Citizen


@admin.register(Citizen)
class ComplaintAdmin(admin.ModelAdmin):
    fieldsets = (
        # (None, {'fields': ('user', )}),
        ('Заявка', {'fields': (
            'title', 'description', 'latitude', 'longitude', 'photo')}),
        ('Состояние', {'fields': ('status', 'updated_at', 'created_at')}),
    )
    list_filter = ('status', 'created_at', 'updated_at')
    search_fields = ('id', 'title', 'description')
    readonly_fields = ('created_at', 'updated_at')
