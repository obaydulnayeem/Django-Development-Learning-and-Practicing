# Generated by Django 4.2.3 on 2023-10-26 10:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('study', '0005_course_university_alter_course_credit'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='uploaded_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='question',
            name='exam_name',
            field=models.CharField(choices=[('1st Mid', '1st Mid Term'), ('2nd Mid', '2nd Mid Term'), ('3rd Mid', '3rd Mid Term'), ('Class Test', 'Class Test'), ('Lab Test', 'Lab Test'), ('Lab Final', 'Lab Final'), ('Semester/Year Final', 'Semester/Year Final')], max_length=50),
        ),
    ]