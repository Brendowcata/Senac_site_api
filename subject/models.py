import uuid
from django.db import models

class SubjectModel(models.Model):
    id = models.UUIDField(
        db_column="id", 
        primary_key=True, 
        editable=False, 
        unique=True, 
        default= uuid.uuid4
        )

    name = models.CharField(
        max_length=50, 
        db_column="NAME"
        ) #Nome

    description = models.TextField(
        db_column="DESCRIPTION"
        ) #Descrição

    class Meta:
        ordering = ['name']
        db_table = "SUBJECT"
        verbose_name = "subject"
        verbose_name_plural = "subjects"

    def __str__(self) -> str:
         return f'{self.name}'

