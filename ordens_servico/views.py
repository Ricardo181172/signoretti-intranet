from rest_framework import generics
from .models import OrdemServico
from rest_framework.permissions import IsAuthenticated
from core.permissions import GlobalDefaultPersmissionClass
from .serializers import OrdemServicoSerializer

class OrdemServicoCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPersmissionClass,)
    queryset = OrdemServico.objects.all()
    serializer_class = OrdemServicoSerializer

class OrdemServicoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPersmissionClass,)
    queryset = OrdemServico.objects.all()
    serializer_class = OrdemServicoSerializer
