from django.db import models

class Voluntario(models.Model):
    nome_completo = models.CharField(max_length=150, verbose_name="Nome Completo")
    cpf = models.CharField(max_length=14, unique=True, verbose_name="CPF")
    data_nascimento = models.DateField(verbose_name="Data de Nascimento")
    email = models.EmailField(unique=True, verbose_name="E-mail")
    telefone = models.CharField(max_length=20, blank=True)
    
    AREAS_CHOICES = [
        ('SAUDE', 'Saúde'),
        ('EDUCACAO', 'Educação'),
        ('LOGISTICA', 'Logística'),
        ('TI', 'Tecnologia'),
        ('COMUNICACAO', 'Comunicação e Marketing'),
    ]
    
    area_atuacao = models.CharField(
        max_length=50, 
        choices=AREAS_CHOICES,
        default='LOGISTICA',
        verbose_name="Área de Atuação preferida"
    )
    
    experiencia = models.TextField(
        blank=True, 
        verbose_name="Por que você quer ser voluntário(a) e quais suas experiências prévias?",
        help_text="Fale um pouco sobre você."
    )
    
    ativo = models.BooleanField(default=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome_completo
