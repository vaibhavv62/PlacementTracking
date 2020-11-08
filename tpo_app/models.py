from django.db import models

# Create your models here.
class Jobs(models.Model):
    company = models.CharField(max_length=50)
    job_pos = models.CharField(max_length=50)
    job_loc = models.CharField(max_length=50)
    ctc_offered = models.FloatField()
    service_agg = models.IntegerField()
    date_of_joining = models.CharField(max_length=50)
    skills_req = models.CharField(max_length=500)
    selection_proc = models.CharField(max_length=500)
    date_of_campus = models.CharField(max_length=50)
    campus_venue = models.CharField(max_length=50)
    age = models.IntegerField()
    passing_yr = models.IntegerField()
    xth_percentage = models.FloatField()
    xiith_percentage = models.FloatField()
    diploma_percentage = models.FloatField()
    engg_cgpa = models.FloatField()
    no_of_dead_kt = models.IntegerField()
    no_of_live_kt = models.IntegerField()
    no_of_yg = models.IntegerField()
    reg_link = models.URLField()
