import uuid
from django.db import models
from course.models import CourseModel

class School_ProgramModel(models.Model):

    id = models.UUIDField(db_column="id", primary_key=True, editable=False, unique=True, default= uuid.uuid4)
    phase = models.PositiveIntegerField(db_column="PHASE") #Fase
    description = models.TextField(db_column="DESCRIPTION") #Descrição
    courses = models.OneToOneField(CourseModel, on_delete=models.CASCADE, null=False, db_column="COURSES") #Cursos

    class Meta:
        ordering = ['phase']
        db_table = "SCHOOL_PROGRAM"
        verbose_name = "school_program"
        verbose_name_plural = "school_programs"

    def __str__(self) -> str:
         return f'{self.phase}'
