from django.test import TestCase
from .models import Voluntario

class VoluntarioModelTest(TestCase):
    def test_criacao_voluntario(self):
        voluntario = Voluntario.objects.create(
            nome_completo="João da Silva",
            cpf="111.222.333-44",
            data_nascimento="1990-01-01",
            email="joao@teste.com",
            area_atuacao="TI"
        )
        self.assertTrue(voluntario.ativo)
        self.assertEqual(str(voluntario), "João da Silva")
