from rest_framework import serializers
from core.models import Pet

class PetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pet
        fields = (
            'id', 'user', 'city', 'email', 'phone',
            'description', 'photo', 'end_date',
            'begin_date', 'active'
        )