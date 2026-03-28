from rest_framework import serializers
from skills.models import Skill
class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'title', 'description', 'difficulty', 'estimated_hours', 'category', 'created_at']
        read_only_fields = ['id', 'created_at']