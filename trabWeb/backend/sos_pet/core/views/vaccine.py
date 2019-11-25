from rest_framework import generics

from core.models import Vaccine
from core.serializers import VaccineSerializer

class VaccineList(generics.ListAPIView):
    queryset = Vaccine.objects.all()
    serializer_class = VaccineSerializer
    permission_classes = ()