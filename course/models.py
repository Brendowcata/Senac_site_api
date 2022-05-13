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
    name = models.CharField(max_length=100, db_column="NAME")
    description = models.CharField(max_length=250, db_column="DESCRIPTION")
    course_type = models.CharField(max_length=50, db_column="COURSE_TYPE")
    course_objective = models.CharField(max_length=250, db_column="COURSE_OBJETIVE")
    curriculum = models.ImageField(blank = True, db_column="CURRICULUM")
    completion_profile = models.CharField(max_length=100, db_column="COMPLETION_PROFILE")
    duration_time = models.CharField(max_length=5, db_column="DURATION_TIME")
    occupation_area = models.CharField(max_length=50, db_column="OCCUPATION_AREA")
    modality = models.CharField(max_length=50, db_column="MODALITY")
    value = models.FloatField(db_column="VALUE")
    is_activate = models.BooleanField(db_column="IS_ACTIVE")
    enrollment = models.BooleanField(db_column="ENROLLMENT")
    mec_score =  models.CharField(max_length=2, choices=MECS.choices, blank=False, null=False, db_column="MEC_SCORE")

    class Meta:
        ordering = ['name']
        db_table = "COURSE"
        verbose_name = "course"
        verbose_name_plural = "courses"

    def __str__(self) -> str:
         return f'{self.name}'

