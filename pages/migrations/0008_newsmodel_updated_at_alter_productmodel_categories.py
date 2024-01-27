# Generated by Django 4.2.7 on 2024-01-26 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_remove_productmodel_description_en_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsmodel',
            name='updated_at',
            field=models.DateField(auto_now=True, verbose_name='updated_at'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='categories',
            field=models.ManyToManyField(related_name='products', to='pages.categorymodel'),
        ),
    ]