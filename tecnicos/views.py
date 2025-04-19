from rest_framework import generics
from .models import Tecnico
from rest_framework.permissions import IsAuthenticated
from core.permissions import GlobalDefaultPersmissionClass
from .serializers import TecnicoSerializer

class TecnicoCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPersmissionClass,)
    #queryset = Tecnico.objects.filter(usr_id_licenca__isnull=False).exclude(usr_id_licenca='') 
    queryset = Tecnico.objects.all()   
    serializer_class = TecnicoSerializer

class TecnicoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPersmissionClass,)
    #queryset = Tecnico.objects.filter(usr_id_licenca__isnull=False).exclude(usr_id_licenca='') 
    queryset = Tecnico.objects.all()
    serializer_class = TecnicoSerializer
