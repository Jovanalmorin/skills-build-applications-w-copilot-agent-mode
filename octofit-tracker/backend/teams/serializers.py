from rest_framework import serializers
from .models import Team

class TeamSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='_id', read_only=True)

    class Meta:
        model = Team
        fields = ['id', 'name', 'members', 'created_at']
