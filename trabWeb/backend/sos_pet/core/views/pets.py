from rest_framework import generics, permissions

from core.models import Pet
from core.serializers import PetSerializer,PetCreateSerializer

class PetList(generics.ListAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes = ()

class PetDestroy(generics.DestroyAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetCreateSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )

class PetUpdate(generics.UpdateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )

class PetCreate(generics.CreateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetCreateSerializer
    permission_classes = ()

class PetGet(generics.RetrieveAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes = ()