# Generated by Django 4.2.3 on 2023-10-29 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0005_alter_task_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos/'),
        ),
    ]