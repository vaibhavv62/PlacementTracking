# Generated by Django 3.0 on 2020-04-21 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_register', '0005_auto_20200421_1343'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentprofile',
            name='be1_cgpa',
            field=models.FloatField(default=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentprofile',
            name='be2_cgpa',
            field=models.FloatField(default=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentprofile',
            name='fe1_cgpa',
            field=models.FloatField(default=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentprofile',
            name='fe2_cgpa',
            field=models.FloatField(default=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentprofile',
            name='se1_cgpa',
            field=models.FloatField(default=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentprofile',
            name='se2_cgpa',
            field=models.FloatField(default=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentprofile',
            name='te1_cgpa',
            field=models.FloatField(default=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentprofile',
            name='te2_cgpa',
            field=models.FloatField(default=8),
            preserve_default=False,
        ),
    ]
