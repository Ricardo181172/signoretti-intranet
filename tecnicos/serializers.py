from rest_framework import serializers
from .models import Tecnico

class TecnicoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tecnico
        fields = ['usr_cod_usuario', 'emp_cod_filial', 'usr_nome_usuario', 'usr_login', 'usr_email']