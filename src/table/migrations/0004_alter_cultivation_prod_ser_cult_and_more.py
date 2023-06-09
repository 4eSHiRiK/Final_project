# Generated by Django 4.1.7 on 2023-03-21 06:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0003_alter_prodcultivations_concentration_after_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cultivation',
            name='prod_ser_cult',
            field=models.ForeignKey(
                blank=True, null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to='table.prodseria'),
        ),
        migrations.AlterField(
            model_name='prodcultivations',
            name='cultivation',
            field=models.ForeignKey(
                blank=True, null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to='table.cultivation'),
        ),
        migrations.AlterField(
            model_name='prodsolutions',
            name='solution',
            field=models.ForeignKey(
                blank=True, null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to='table.solution'),
        ),
        migrations.AlterField(
            model_name='solution',
            name='prod_ser_sol',
            field=models.ForeignKey(
                blank=True, null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to='table.prodseria'),
        ),
    ]
