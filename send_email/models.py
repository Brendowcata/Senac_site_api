from django.db import models
from course.models import CourseModel
from university.models import UniversityModel

class Send_EmailModel(models.Model):
    
    name = models.CharField(
        max_length=100, 
        ) #Nome

    email = models.EmailField() #E-mail

    email_university = models.EmailField() #E-mail da Universidade
    
    phone_number = models.CharField(
        max_length=15, 
        blank=True,
        ) #Celular
    
    message = models.TextField(
        null=True,
        blank=True,
    )

    courses = models.ForeignKey(
        CourseModel, 
        on_delete=models.DO_NOTHING, 
        null=True,
        blank=True,
        ) #Cursos
    
    universities = models.ForeignKey(
        UniversityModel,
        on_delete=models.DO_NOTHING,
        null=False,
    ) # Universidades

    class Meta:
        db_table = "SEND_EMAIL"
        verbose_name = "send_email"
        verbose_name_plural = "send_emails"
    
