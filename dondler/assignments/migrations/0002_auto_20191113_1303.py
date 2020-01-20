# Generated by Django 2.2.7 on 2019-11-13 13:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20191113_1241'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('assignments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, max_length=1000, null=True)),
                ('link', models.URLField(blank=True, null=True)),
                ('last_date', models.DateTimeField()),
                ('files', models.FileField(blank=True, null=True, upload_to='assignments/')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Subject')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SubmitAssignments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, max_length=1000, null=True)),
                ('link', models.URLField(blank=True, null=True)),
                ('submission_date', models.DateTimeField(auto_now_add=True)),
                ('files', models.FileField(blank=True, null=True, upload_to='submitted-assignments/')),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assignments.Assignment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Assignments',
        ),
    ]
