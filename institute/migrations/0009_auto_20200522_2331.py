# Generated by Django 3.0.5 on 2020-05-22 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0008_auto_20200501_1403'),
    ]

    operations = [
        migrations.AddField(
            model_name='institutestd',
            name='afd',
            field=models.BinaryField(null=True),
        ),
        migrations.AddField(
            model_name='institutestd',
            name='amount',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='institutestd',
            name='application',
            field=models.BinaryField(null=True),
        ),
        migrations.AddField(
            model_name='institutestd',
            name='bank',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='institutestd',
            name='bgp',
            field=models.CharField(default='B+', max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='institutestd',
            name='caste',
            field=models.CharField(default='OBC', max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='institutestd',
            name='ch_no',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='institutestd',
            name='dop',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='institutestd',
            name='emr_phone',
            field=models.IntegerField(default=124578),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='institutestd',
            name='ph_phone',
            field=models.IntegerField(default=235689),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='institutestd',
            name='photo',
            field=models.BinaryField(null=True),
        ),
        migrations.AddField(
            model_name='institutestd',
            name='recipt',
            field=models.BinaryField(null=True),
        ),
        migrations.AddField(
            model_name='institutestd',
            name='undertake',
            field=models.BinaryField(null=True),
        ),
    ]
