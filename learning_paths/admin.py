from django.contrib import admin
from learning_paths.models import LearningPath
@admin.register(LearningPath)
class LearningPathAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at')
    search_fields = ('title', 'description','skils__name')
    list_filter = ('created_at',)
    #@staticmethod
    #def get_queryset(request):
    #    return LearningPath.objects.prefetch_related('skils')

