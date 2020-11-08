from django.contrib import admin

# Register your models here.
from tpo_app.models import Jobs


class JobsAdmin(admin.ModelAdmin):
    list_display = ['company','job_pos','job_loc','ctc_offered','engg_cgpa']

admin.site.register(Jobs,JobsAdmin)