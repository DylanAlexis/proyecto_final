# Generated by Django 4.0.4 on 2022-07-05 08:28

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('appHospital', '0007_alter_blog_image_alter_especialidad_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='especialidad',
            name='descripcion',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='especialidad',
            name='id',
            field=models.CharField(default=uuid.UUID('314055d5-fa65-4ffc-9abc-7e712beee5ec'), max_length=40, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='id',
            field=models.CharField(default=uuid.UUID('c587b78b-775b-48b7-8900-f67356caad16'), max_length=40, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='profesional',
            name='id',
            field=models.CharField(default=uuid.UUID('08151c1c-f27b-4dcc-bd35-2a9963cbe404'), max_length=40, primary_key=True, serialize=False),
        ),
    ]