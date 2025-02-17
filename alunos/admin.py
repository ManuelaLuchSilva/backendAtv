from django.contrib import admin
from .models import Estado, Cidade, Aluno, Paciente, Medico, Consulta

admin.site.register(Estado)
admin.site.register(Cidade)
admin.site.register(Aluno)
admin.site.register(Paciente)
admin.site.register(Medico)
admin.site.register(Consulta)
