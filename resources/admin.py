from django.contrib import admin
from resources.models import Resource
@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'resource_type', 'created_at')
    search_fields = ('title', 'resource_type','skills__name')
    list_filter = ('resource_type', 'created_at')
    ordering = ('resource_type', 'title')
