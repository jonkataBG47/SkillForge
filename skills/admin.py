from django.contrib import admin

from skills.models import Skill

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('title','category','difficulty','created_at','estimated_hours')
    search_fields = ('title', 'category__name','description')
    list_filter = ('difficulty', 'category')
    ordering = ('estimated_hours','created_at')

