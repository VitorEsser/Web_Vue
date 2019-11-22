from rest_framework import generics

from core.models import Pet
from core.serializers import PetSerializer

class PetList(generics.ListAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes = ()