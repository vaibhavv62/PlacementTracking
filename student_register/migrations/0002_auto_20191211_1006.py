# Generated by Django 3.0 on 2019-12-11 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_register', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
