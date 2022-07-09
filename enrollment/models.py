import uuid
from django.db import models

from course.models import CourseModel
from university.models import UniversityModel

class EnrollmentModel(models.Model):

    id = models.UUIDField(
        db_column="id", 
        primary_key=True, 
        editable=False, 
        unique=True, 
        default= uuid.uuid4
        )

    date_initial = models.DateField(
        db_column="DATE_INITIAL"
        ) # Data inicial
    
    date_final = models.DateField(
        db_column="DATE_FINAL"
        ) #Data final

    courses = models.ForeignKey(
        CourseModel, 
        on_delete=models.CASCADE, 
        null=False,
        related_name='enrollments',
        db_column="COURSES"
        ) #Cursos
    
    universities = models.ForeignKey(
        UniversityModel,
        on_delete=models.DO_NOTHING,
        null=False,
        db_column="UNIVERSITIES"
    ) # Universidades

    class Meta:
        db_table = "ENROLLMENT"
        verbose_name = "enrollment"
        verbose_name_plural = "enrollments"

    def __str__(self) -> str:
         return f'{self.date_initial.strftime("%m/%d/%Y")} - {self.date_final.strftime("%m/%d/%Y")}'
