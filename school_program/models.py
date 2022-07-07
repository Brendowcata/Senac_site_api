import uuid
from django.db import models
from course.models import CourseModel
from subject.models import SubjectModel

class School_ProgramModel(models.Model):

    id = models.UUIDField(
        db_column="id", 
        primary_key=True, 
        editable=False, 
        unique=True, 
        default= uuid.uuid4
        )

    phase = models.PositiveIntegerField(
        db_column="PHASE"
        ) #Fase
    
    phase_time = models.PositiveIntegerField(
        db_column="PHASE_TIME"
        ) #Tempo de fase

    courses = models.ForeignKey(
        CourseModel, 
        on_delete=models.CASCADE, 
        null=False, 
        related_name='school_programs',
        db_column="COURSES"
        ) #Cursos

    subjects = models.ManyToManyField(
        SubjectModel,
        blank=True
        ) #Matérias

    
    class Meta:
        db_table = "SCHOOL_PROGRAM"
        verbose_name = "school_program"
        verbose_name_plural = "school_programs"

    def __str__(self) -> str:
         return f'{self.phase}'
