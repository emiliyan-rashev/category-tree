# Generated by Django 4.0.2 on 2022-02-26 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_category_image_category_similar_to_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
