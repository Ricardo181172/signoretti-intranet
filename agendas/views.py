from typing import Any
from django.views.generic import ListView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from core.permissions import GlobalDefaultPersmissionClass
from .models import Agenda
from . import models
from .serializers import AgendaSerializer

class AgendaListView(ListView):
    model = models.Agenda
    template_name = 'agenda_list.html'
    context_object_name = 'agendas'

    def get_queryset(self):
        queryset = super().get_queryset()
        emp_cod_filial = self.request.GET.get('emp_cod_filial')

        if emp_cod_filial:
            queryset = queryset.filter(emp_cod_filial__icontains=emp_cod_filial)
        
        return queryset

class AgendaCreateListView(generics.ListCreateAPIView):
     permission_classes = (IsAuthenticated, GlobalDefaultPersmissionClass,)
     queryset = Agenda.objects.all()
     serializer_class = AgendaSerializer

# class AgendaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = (IsAuthenticated, GlobalDefaultPersmissionClass,)
#     queryset = Agenda.objects.all()
#     serializer_class = AgendaSerializer