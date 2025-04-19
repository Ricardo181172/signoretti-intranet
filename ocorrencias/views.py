from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from core.permissions import GlobalDefaultPersmissionClass
from .models import Ocorrencia
from .serializers import OcorrenciaSerializer


class OcorrenciaCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPersmissionClass,)
    queryset = Ocorrencia.objects.all()
    serializer_class = OcorrenciaSerializer

class OcorrenciaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPersmissionClass,)
    queryset = Ocorrencia.objects.all()
    serializer_class = OcorrenciaSerializer    
