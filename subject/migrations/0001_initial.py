# Generated by Django 4.0.4 on 2022-05-18 00:52

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SubjectModel',
            fields=[
                ('id', models.UUIDField(db_column='id', default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(db_column='NAME', max_length=50)),
                ('subject_time', models.PositiveIntegerField(db_column='SUBJECT_TIME')),
                ('description', models.TextField(db_column='DESCRIPTION')),
            ],
            options={
                'verbose_name': 'subject',
                'verbose_name_plural': 'subjects',
                'db_table': 'SUBJECT',
                'ordering': ['name'],
            },
        ),
    ]
