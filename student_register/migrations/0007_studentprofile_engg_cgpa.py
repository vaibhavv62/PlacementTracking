# Generated by Django 3.0 on 2020-04-21 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_register', '0006_auto_20200421_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentprofile',
            name='engg_cgpa',
            field=models.FloatField(default=7.48),
            preserve_default=False,
        ),
    ]