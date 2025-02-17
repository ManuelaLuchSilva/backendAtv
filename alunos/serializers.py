from rest_framework.serializers import ModelSerializer
from .models import Estado
from .models import Cidade
from .models import Aluno
from .models import Paciente
from .models import Medico
from .models import Consulta

class EstadoSerializer(ModelSerializer):
    class Meta:
        model = Estado
        fields = '__all__'

class CidadeSerializer(ModelSerializer):
    class Meta:
        model = Cidade
        fields = '__all__'

class AlunoSerializer(ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'
    
class PacienteSerializer(ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'

class MedicoSerializer(ModelSerializer):
    class Meta:
        model = Medico
        fields = '__all__'

class ConsultaSerializer(ModelSerializer):
    class Meta:
        model = Consulta
        fields = '__all__'