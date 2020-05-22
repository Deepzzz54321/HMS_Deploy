# Generated by Django 3.0.5 on 2020-05-22 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaints', '0008_auto_20200514_0253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='officialcomplaints',
            name='type',
            field=models.CharField(choices=[('General', 'General'), ('Food Issues', 'Food Issues'), ('Electrical', 'Electrical'), ('Civil', 'Civil'), ('Room Cleaning', 'Room Cleaning'), ('Restroom Cleaning', 'Restroom Cleaning'), ('Indisciplinary', 'Indisciplinary'), ('Discrimination/Harassment', 'Discrimination/Harassment'), ('Damage to property', 'Damage to property'), ('Latecomer', 'Latecomer')], max_length=40),
        ),
    ]
