# Generated by Django 4.1.7 on 2023-04-13 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0006_prodspec_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(
                blank=True, height_field=200,
                null=True, upload_to='', width_field=200),
        ),
    ]
