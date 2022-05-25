import uuid
from django.db import models

class EnrollmentModel(models.Model):

    id = models.UUIDField(
        db_column="id", 
        primary_key=True, 
        editable=False, 
        unique=True, 
        default= uuid.uuid4
        )

    is_activate = models.BooleanField(
        default=True, 
        db_column="IS_ACTIVE"
        ) #Se as incrições estão abertas

    date_initial = models.DateField(
        db_column="DATE_INITIAL"
        )
    
    date_final = models.DateField(
        db_column="DATE_FINAL"
        )

    class Meta:
        ordering = ['is_activate']
        db_table = "ENROLLMENT"
        verbose_name = "enrollment"
        verbose_name_plural = "enrollments"

    def __str__(self) -> str:
         return f'{self.date_initial.strftime("%m/%d/%Y")} - {self.date_final.strftime("%m/%d/%Y")}'
