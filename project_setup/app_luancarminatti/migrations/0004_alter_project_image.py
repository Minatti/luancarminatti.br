# Generated by Django 4.2.6 on 2023-10-12 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_luancarminatti', '0003_remove_project_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
