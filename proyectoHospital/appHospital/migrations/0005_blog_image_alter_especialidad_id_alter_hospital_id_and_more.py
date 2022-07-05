# Generated by Django 4.0.4 on 2022-07-04 09:16

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('appHospital', '0004_alter_blog_slug_alter_especialidad_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(default='none.jpg', upload_to=''),
        ),
        migrations.AlterField(
            model_name='especialidad',
            name='id',
            field=models.CharField(default=uuid.UUID('263849e6-a5cb-4a82-811a-52be099b88a7'), max_length=40, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='id',
            field=models.CharField(default=uuid.UUID('549d7491-1cc8-4973-86d3-b485361bd5bc'), max_length=40, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='profesional',
            name='id',
            field=models.CharField(default=uuid.UUID('c2c52158-1dbe-4d52-a457-a8125b4d3525'), max_length=40, primary_key=True, serialize=False),
        ),
    ]
