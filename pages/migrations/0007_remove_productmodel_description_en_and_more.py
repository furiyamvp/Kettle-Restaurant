# Generated by Django 4.2.7 on 2024-01-24 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_productmodel_description_en_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productmodel',
            name='description_en',
        ),
        migrations.RemoveField(
            model_name='productmodel',
            name='description_uz',
        ),
        migrations.RemoveField(
            model_name='productmodel',
            name='title_en',
        ),
        migrations.RemoveField(
            model_name='productmodel',
            name='title_uz',
        ),
        migrations.AlterField(
            model_name='categorymodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='categorymodel',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='categorymodel',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
