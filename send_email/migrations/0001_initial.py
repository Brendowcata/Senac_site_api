# Generated by Django 4.0.5 on 2022-07-06 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0001_initial'),
        ('university', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Send_EmailModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('email_university', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(blank=True, max_length=15)),
                ('message', models.TextField(blank=True, null=True)),
                ('courses', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='course.coursemodel')),
                ('universities', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='university.universitymodel')),
            ],
            options={
                'verbose_name': 'send_email',
                'verbose_name_plural': 'send_emails',
                'db_table': 'SEND_EMAIL',
            },
        ),
    ]
