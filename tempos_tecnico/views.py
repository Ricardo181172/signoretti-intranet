from rest_framework import generics
from .models import TemposTecnico
from rest_framework.permissions import IsAuthenticated
from core.permissions import GlobalDefaultPersmissionClass
from .serializers import TemposTecnicoSerializer

class TemposTecnicoCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPersmissionClass,)
    queryset = TemposTecnico.objects.all()
    serializer_class = TemposTecnicoSerializer

class TemposTecnicoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPersmissionClass,)
    queryset = TemposTecnico.objects.all()
    serializer_class = TemposTecnicoSerializer

