# Generated by Django 4.1.7 on 2023-03-16 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cultivation',
            old_name='name_cult',
            new_name='name_of_cultivation',
        ),
        migrations.RenameField(
            model_name='equipment',
            old_name='name_equip_all',
            new_name='name_current_equipment',
        ),
        migrations.RenameField(
            model_name='prodsolutions',
            old_name='ser_sol',
            new_name='solution_seria',
        ),
        migrations.RenameField(
            model_name='solution',
            old_name='name_sol',
            new_name='name_of_solution',
        ),
    ]
