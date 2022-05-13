import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _

from course.models import CourseModel

class UniversityModel(models.Model):

    class STATES(models.TextChoices):
        AC = 'AC', _('Acre')
        AL = 'AL', _('Alagoas')
        AP = 'AP', _('Amapa')
        AM = 'AM', _('Amazonas')
        BA = 'BA', _('Bahia')
        CE = 'CE', _('Ceara')
        ES = 'ES', _('Espirito Santo')
        GO = 'GO', _('Goias')
        MA = 'MA', _('Maranhão')
        MT = 'MT', _('Mato Grosso')
        MS = 'MS', _('Mato Grosso do Sul')
        MG = 'MG', _('Minas Gerais')
        PA = 'PA', _('Para')
        PB = 'PB', _('Paraiba')
        PR = 'PR', _('Parana')
        PE = 'PE', _('Pernambuco')
        PI = 'PI', _('Piaui')
        RJ = 'RJ', _('Rio de Janeiro')
        RN = 'RN', _('Rio Grande do Norte')
        RS = 'RS', _('Rio Grande Do Sul')
        RO = 'RO', _('Rondônia')
        RR = 'RR', _('Roraima')
        SC = 'SC', _('Santa Catarina')
        SP = 'SP', _('São Paulo')
        SE = 'SE', _('Sergipe')
        TO = 'TO', _('Tocantins')
        DF = 'DF', _('Distrito Federal')

    id = models.UUIDField(db_column="id", primary_key=True, editable=False, unique=True, default= uuid.uuid4)
    name = models.CharField(max_length=100, db_column="NAME")
    telephone = models.CharField(max_length=14, db_column="TELEPHONE")
    phone_number = models.CharField(max_length=15, db_column="PHONE_NUMBER")
    email = models.EmailField(db_column="EMAIL")
    street = models.CharField(max_length=100, db_column="STREET")
    neighborhood = models.CharField(max_length=100, db_column="NEIGHBOURHOOD")
    city = models.CharField(max_length=50, db_column="CITY")
    state = models.CharField(max_length=2, choices=STATES.choices, blank=False, null=False, db_column="STATE")
    zip_code = models.CharField(max_length=8, db_column="ZIP_CODE")
    house_number = models.CharField(max_length=5, db_column="HOUSE_NUMBER")
    courses = models.ManyToManyField(CourseModel)

    class Meta:
        ordering = ['name']
        db_table = "UNIVERSITY"
        verbose_name = "university"
        verbose_name_plural = "universities"

    def __str__(self) -> str:
         return f'{self.name}'