# Generated by Django 4.1.7 on 2023-04-04 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0005_prodequipment_image_prodseria_total_result_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='prodspec',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
