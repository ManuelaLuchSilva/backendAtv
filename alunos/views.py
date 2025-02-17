from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Estado
from .models import Cidade
from .models import Aluno
from .models import Medico
from .models import Consulta
from .models import Paciente
from .serializers import EstadoSerializer
from .serializers import CidadeSerializer
from .serializers import AlunoSerializer
from .serializers import ConsultaSerializer
from .serializers import MedicoSerializer
from .serializers import PacienteSerializer

class EstadoViewSet(ModelViewSet):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer

class CidadeViewSet(ModelViewSet):
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer

class AlunoViewSet(ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class MedicoViewSet(ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer

class PacienteViewSet(ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class ConsultaViewSet(ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer