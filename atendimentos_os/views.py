from django.db.models import Max, Subquery, OuterRef
from rest_framework import generics, views, response, status
from rest_framework.permissions import IsAuthenticated
from core.permissions import GlobalDefaultPersmissionClass
from .models import AtendimentoOS
from .serializers import AtendimentoOSSerializer


class AtendimentoOSCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPersmissionClass,)
    queryset = AtendimentoOS.objects.all()
    serializer_class = AtendimentoOSSerializer

class AtendimentoOSRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPersmissionClass,)
    queryset = AtendimentoOS.objects.all()
    serializer_class = AtendimentoOSSerializer

class AtendimentoOSStatsView(views.APIView):
     permission_classes = (IsAuthenticated, GlobalDefaultPersmissionClass,)     
     
     def get(self, request):
        """
        Retorna o registro mais recente de atendimento para cada usuário.
        """
        subquery = AtendimentoOS.objects.filter(
            usr_cod_usuario=OuterRef('usr_cod_usuario')
        ).order_by('-atd_dth_primeiro_ocorrencia').values('pk')[:1]

        atendimentos_recentes = AtendimentoOS.objects.filter(
            pk__in=Subquery(subquery)
        )

        return response.Response(
            data={
                'atendimentos_recentes': atendimentos_recentes,                
            },
            status=status.HTTP_200_OK)