import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _

class CourseModel(models.Model):

    class MECS(models.TextChoices):
        M1 = '1', _('MEC_SCORE_1')
        M2 = '2', _('MEC_SCORE_2')
        M3 = '3', _('MEC_SCORE_3')
        M4 = '4', _('MEC_SCORE_4')
        M5 = '5', _('MEC_SCORE_5')

    id = models.UUIDField(db_column="id", primary_key=True, editable=False, unique=True, default= uuid.uuid4)
    name = models.CharField(max_length=100, db_column="NAME") #Nome
    banner = models.ImageField(blank=True, db_column="BANNER") #Imagem do curso
    description = models.CharField(max_length=250, db_column="DESCRIPTION") #Descrição
    course_type = models.CharField(max_length=50, db_column="COURSE_TYPE") #Tipo de curso
    course_objective = models.CharField(max_length=250, db_column="COURSE_OBJETIVE") #Objetivo do curso
    curriculum = models.ImageField(blank = True, db_column="CURRICULUM") #Grade curricular *Imagem
    completion_profile = models.CharField(max_length=100, db_column="COMPLETION_PROFILE") #Perfil de conclusão
    duration_time = models.CharField(max_length=5, db_column="DURATION_TIME") # tempo de duração
    occupation_area = models.CharField(max_length=50, db_column="OCCUPATION_AREA") #area de atuação
    modality = models.CharField(max_length=50, db_column="MODALITY") #modalidade
    value = models.FloatField(db_column="VALUE") #valor do curso
    is_activate = models.BooleanField(db_column="IS_ACTIVE") #Se o Curso está ativo
    enrollment = models.BooleanField(db_column="ENROLLMENT") #Se as inscrições estão abertas
    mec_score =  models.CharField(max_length=2, choices=MECS.choices, blank=False, null=False, db_column="MEC_SCORE") #Nota do mec

    class Meta:
        ordering = ['name']
        db_table = "COURSE"
        verbose_name = "course"
        verbose_name_plural = "courses"

    def __str__(self) -> str:
         return f'{self.name}'

