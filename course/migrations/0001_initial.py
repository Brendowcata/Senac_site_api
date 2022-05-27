# Generated by Django 4.0.4 on 2022-05-27 02:38

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CourseModel',
            fields=[
                ('id', models.UUIDField(db_column='id', default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(db_column='NAME', max_length=100)),
                ('description', models.TextField(db_column='DESCRIPTION')),
                ('course_type', models.CharField(choices=[('GRADUACAO', 'Graduação'), ('POS_GRADUACAO', 'Pós-Graduação')], db_column='COURSE_TYPE', default='GRADUACAO', max_length=50)),
                ('course_objective', models.TextField(db_column='COURSE_OBJETIVE')),
                ('curriculum', models.ImageField(blank=True, db_column='CURRICULUM', upload_to='')),
                ('completion_profile', models.TextField(db_column='COMPLETION_PROFILE')),
                ('duration_time', models.PositiveIntegerField(db_column='DURATION_TIME')),
                ('occupation_area', models.CharField(db_column='OCCUPATION_AREA', max_length=50)),
                ('modality', models.CharField(choices=[('PRESENCIAL', 'Educação Presencial'), ('EAD', 'Educação a distância ("EAD")'), ('HIBRIDO', 'Educação Híbrida ')], db_column='MODALITY', default='PRESENCIAL', max_length=10)),
                ('value', models.FloatField(db_column='VALUE')),
                ('is_activate', models.BooleanField(db_column='IS_ACTIVE', default=True)),
                ('mec_score', models.CharField(choices=[('MEC5', 'NOTA 5 DO MEC'), ('MEC4', 'NOTA 4 DO MEC'), ('MEC3', 'NOTA 3 DO MEC'), ('MEC2', 'NOTA 2 DO MEC'), ('MEC1', 'NOTA 1 DO MEC')], db_column='MEC_SCORE', default='MEC5', max_length=4)),
            ],
            options={
                'verbose_name': 'course',
                'verbose_name_plural': 'courses',
                'db_table': 'COURSE',
                'ordering': ['name'],
            },
        ),
    ]
