from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from skills.models import Skill
from skills.serializer import SkillSerializer


class SkillApiView(ListCreateAPIView):
    serializer_class = SkillSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Skill.objects.filter(user=self.request.user).order_by('-created_at', 'title')
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)