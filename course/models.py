import uuid
from django.db import models

class CourseModel(models.Model):

    MODALITYS = (
        ('PRESENCIAL', 'Educação Presencial'),
        ('HIBRIDO', 'Educação Híbrida '),
        ('EAD', 'Educação a Distância')
    )

    MECS = (
        ('MEC5', 'NOTA 5 DO MEC'),
        ('MEC4', 'NOTA 4 DO MEC'),
        ('MEC3', 'NOTA 3 DO MEC'),
        ('MEC2', 'NOTA 2 DO MEC'),
        ('MEC1', 'NOTA 1 DO MEC')
    )

    TYPES_COURSES = (
        ('GRADUACAO', 'Graduação'),
        ('POS_GRADUACAO', 'Pós-Graduação'),
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

    course_type = models.CharField(
        max_length=13, 
        choices=TYPES_COURSES,
        blank=False,
        null=False,
        default="GRADUACAO",
        db_column="COURSE_TYPE"
        ) #Tipo de curso Graduação/Pós-Graduação

    course_objective = models.TextField(
        db_column="COURSE_OBJECTIVE"
        ) #Objetivo do curso

    curriculum = models.ImageField(
        blank = True, 
        db_column="CURRICULUM") #Grade curricular *Imagem

    completion_profile = models.TextField(
        db_column="COMPLETION_PROFILE"
        ) #Perfil de conclusão

    duration_time = models.PositiveIntegerField(
        db_column="DURATION_TIME"
        ) # tempo de duração

    occupation_area = models.CharField(
        max_length=50, 
        db_column="OCCUPATION_AREA"
        ) #area de atuação

    modality = models.CharField(
        max_length=10, 
        choices=MODALITYS, 
        blank=False, 
        null=False, 
        default='PRESENCIAL', 
        db_column="MODALITY"
        ) #modalidade
    
    course_image = models.ImageField(
        blank=True, 
        db_column="COURSE_IMAGE"
        ) #imagem do curso

    is_activate = models.BooleanField(
        default=True, 
        db_column="IS_ACTIVE"
        ) #Se o Curso está ativo


    mec_score =  models.CharField(
        max_length=4, 
        choices=MECS, 
        blank=False, 
        null=False, 
        default='MEC5',  
        db_column="MEC_SCORE"
        ) #Nota do mec

    class Meta:
        db_table = "COURSE"
        verbose_name = "course"
        verbose_name_plural = "courses"

    def __str__(self) -> str:
         return f'{self.name}'

