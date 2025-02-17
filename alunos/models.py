from django.db import models

class Estado(models.Model):
    nome = models.CharField(max_length=50)
    sigla = models.CharField(max_length=2)

    def __str__(self):
        return f'{self.nome} - {self.sigla}'
    
class Cidade(models.Model):
    nome = models.CharField(max_length=50)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.nome} - {self.estado.sigla}'
    
class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.nome} - {self.cidade.nome} ({self.cidade.estado.sigla})'

class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()    
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.nome} - {self.telefone}'

class Medico(models.Model):
    nome = models.CharField(max_length=100)
    especialidade = models.CharField(max_length=100)
    crm = models.CharField(max_length=9)

    def __str__(self):
        return f'{self.nome} - {self.crm}'

class Consulta(models.Model):
    id_paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT)
    id_medico = models.ForeignKey(Medico, on_delete=models.PROTECT)
    data_consulta = models.DateField()
    descricao = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.id_medico.nome} - {self.id_paciente.nome} - {self.data_consulta}'
