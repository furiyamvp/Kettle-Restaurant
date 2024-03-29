# Generated by Django 4.2.7 on 2024-01-11 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_workermodel_alter_newsmodel_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('photo', models.ImageField(upload_to='')),
                ('ingredient', models.CharField(max_length=460)),
            ],
            options={
                'verbose_name': 'gallery',
                'verbose_name_plural': 'galleries',
            },
        ),
    ]
