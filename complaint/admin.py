from django.contrib import admin
from complaint.models import Complaint


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    fieldsets = (
        # (None, {'fields': ('user', )}),
        ('Заявка', {'fields': ('title', 'description')}),
        ('Состояние', {'fields': ('status', 'updated_at', 'created_at')}),
    )
    list_filter = ('status', 'created_at', 'updated_at')
    search_fields = ('id', 'title', 'description')
    readonly_fields = ('created_at', 'updated_at')
