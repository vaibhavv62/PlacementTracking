# Generated by Django 3.0 on 2020-04-04 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_register', '0002_auto_20191211_1006'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clg_email', models.EmailField(max_length=254)),
                ('fname', models.CharField(max_length=15)),
                ('mname', models.CharField(max_length=15)),
                ('lname', models.CharField(max_length=15)),
                ('clg', models.CharField(max_length=40)),
                ('prn', models.CharField(max_length=40)),
                ('branch', models.CharField(max_length=40)),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=10)),
                ('native_place', models.CharField(max_length=20)),
                ('mother_tounge', models.CharField(max_length=20)),
                ('other_lang', models.CharField(max_length=20)),
                ('mono1', models.CharField(max_length=20)),
                ('mono2', models.CharField(max_length=20)),
                ('parent_mono1', models.CharField(max_length=20)),
                ('parent_mono2', models.CharField(max_length=20)),
                ('personal_email', models.EmailField(max_length=254)),
                ('parent_email', models.EmailField(max_length=254)),
                ('xth_board', models.CharField(max_length=20)),
                ('xth_passing_yr', models.IntegerField()),
                ('xth_marks_obtained', models.IntegerField()),
                ('xth_marks_outoff', models.IntegerField()),
                ('xiith_board', models.CharField(max_length=20)),
                ('xiith_passing_yr', models.IntegerField()),
                ('xiith_marks_obtained', models.IntegerField()),
                ('xiith_marks_outoff', models.IntegerField()),
                ('diploma_clg', models.CharField(max_length=20)),
                ('diploma_passing_yr', models.IntegerField()),
                ('diploma_marks_obtained', models.IntegerField()),
                ('diploma_marks_outoff', models.IntegerField()),
                ('fe1_tot_credits', models.IntegerField()),
                ('fe1_tot_credits_obtained', models.IntegerField()),
                ('fe2_tot_credits', models.IntegerField()),
                ('fe2_tot_credits_obtained', models.IntegerField()),
                ('se1_tot_credits', models.IntegerField()),
                ('se1_tot_credits_obtained', models.IntegerField()),
                ('se2_tot_credits', models.IntegerField()),
                ('se2_tot_credits_obtained', models.IntegerField()),
                ('te1_tot_credits', models.IntegerField()),
                ('te1_tot_credits_obtained', models.IntegerField()),
                ('te2_tot_credits', models.IntegerField()),
                ('te2_tot_credits_obtained', models.IntegerField()),
                ('no_of_dead_kt', models.IntegerField()),
                ('no_of_live_kt', models.IntegerField()),
                ('no_of_yd_engg', models.IntegerField()),
                ('no_of_yd_diploma', models.IntegerField()),
                ('no_of_yg', models.IntegerField()),
                ('plan_after_engg', models.CharField(max_length=20)),
                ('te_mini_proj_company', models.CharField(max_length=20)),
                ('te_mini_proj_title', models.CharField(max_length=20)),
                ('certification1', models.CharField(max_length=20)),
                ('certification2', models.CharField(max_length=20)),
                ('AddOnCourse1', models.CharField(max_length=20)),
                ('AddOnCourse2', models.CharField(max_length=20)),
                ('aadhar_no', models.CharField(max_length=20)),
            ],
        ),
    ]