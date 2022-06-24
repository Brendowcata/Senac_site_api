import uuid
from django.db import models

from course.models import CourseModel

class UniversityModel(models.Model):

    STATES = (
        ('SC', 'Santa Catarina'),
        #('AC', 'Acre'),
        #('AL', 'Alagoas'),
        #('AP', 'Amapa'),
        #('AM', 'Amazonas'),
        #('BA', 'Bahia'),
        #('CE', 'Ceara'),
        #('ES', 'Espirito Santo'),
        #('GO', 'Goias'),
        #('MA', 'Maranhão'),
        #('MT', 'Mato Grosso'),
        #('MS', 'Mato Grosso do Sul'),
        #('MG', 'Minas Gerais'),
        #('PA', 'Para'),
        #('PB', 'Paraiba'),
        #('PR', 'Parana'),
        #('PE', 'Pernambuco'),
        #('PI', 'Piaui'),
        #('RJ', 'Rio de Janeiro'),
        #('RN', 'Rio Grande do Norte'),
        #('RS', 'Rio Grande Do Sul'),
        #('RO', 'Rondônia'),
        #('RR', 'Roraima'),
        #('SP', 'São Paulo'),
        #('SE', 'Sergipe'),
        #('TO', 'Tocantins'),
        #('DF', 'Distrito Federal')
    )

    id = models.UUIDField(
        db_column="id", 
        primary_key=True, 
        editable=False, 
        unique=True, 
        default= uuid.uuid4
        )

    name = models.CharField(
        max_length=100, 
        db_column="NAME"
        ) #Nome

    telephone = models.CharField(
        max_length=14,
        blank=True,
        db_column="TELEPHONE"
        ) #Telefone

    phone_number = models.CharField(
        max_length=15, 
        db_column="PHONE_NUMBER"
        ) #Celular

    attendance = models.TextField(
        db_column="ATTENDANCE"
        ) #Atendimento

    email = models.EmailField(
        db_column="EMAIL"
        ) #E-mail

    street = models.CharField(
        max_length=100, 
        db_column="STREET"
        ) #Rua

    neighborhood = models.CharField(
        max_length=100, 
        db_column="NEIGHBORHOOD"
        ) #Bairro

    city = models.CharField(
        max_length=50, 
        db_column="CITY"
        ) #Cidade

    state = models.CharField(
        max_length=2, 
        choices=STATES, 
        blank=False, 
        null=False, 
        db_column="STATE"
        ) #Estado/UF

    zip_code = models.CharField(
        max_length=9, 
        db_column="ZIP_CODE"
        ) #CEP

    house_number = models.CharField(
        max_length=5, 
        db_column="HOUSE_NUMBER"
        ) #Número do local

    university_image_local = models.ImageField(
        blank=True, 
        db_column="UNIVERSITY_IMAGE_LOCAL"
        )

    is_activate = models.BooleanField(
        default=True, 
        db_column="IS_ACTIVE"
        ) #Se a faculdade está ativa

    courses = models.ManyToManyField(
        CourseModel,
        related_name='universities', 
        blank=True,
        ) #Cursos

    class Meta:
        db_table = "UNIVERSITY"
        verbose_name = "university"
        verbose_name_plural = "universities"

    def __str__(self) -> str:
         return f'{self.name}'