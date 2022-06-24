# Generated by Django 4.0.5 on 2022-06-23 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursemodel',
            name='description',
        ),
        migrations.AlterField(
            model_name='coursemodel',
            name='course_objective',
            field=models.TextField(db_column='COURSE_OBJECTIVE'),
        ),
        migrations.AlterField(
            model_name='coursemodel',
            name='course_type',
            field=models.CharField(choices=[('GRADUACAO', 'Graduação'), ('POS_GRADUACAO', 'Pós-Graduação')], db_column='COURSE_TYPE', default='GRADUACAO', max_length=13),
        ),
        migrations.AlterField(
            model_name='coursemodel',
            name='modality',
            field=models.CharField(choices=[('PRESENCIAL', 'Educação Presencial'), ('HIBRIDO', 'Educação Híbrida '), ('EAD', 'Educação a Distância')], db_column='MODALITY', default='PRESENCIAL', max_length=10),
        ),
    ]
