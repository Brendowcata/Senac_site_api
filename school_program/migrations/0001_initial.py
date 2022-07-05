# Generated by Django 4.0.5 on 2022-07-05 23:51

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('subject', '0001_initial'),
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='School_ProgramModel',
            fields=[
                ('id', models.UUIDField(db_column='id', default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('phase', models.PositiveIntegerField(db_column='PHASE')),
                ('phase_time', models.PositiveIntegerField(db_column='PHASE_TIME')),
                ('courses', models.ForeignKey(db_column='COURSES', on_delete=django.db.models.deletion.CASCADE, to='course.coursemodel')),
                ('subjects', models.ManyToManyField(blank=True, to='subject.subjectmodel')),
            ],
            options={
                'verbose_name': 'school_program',
                'verbose_name_plural': 'school_programs',
                'db_table': 'SCHOOL_PROGRAM',
            },
        ),
    ]
