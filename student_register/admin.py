from django.contrib import admin
from .models import Student, StudentProfile
# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display = ['rn', 'name', 'branch', 'mobile', 'te_cgpa']


admin.site.register(Student,StudentAdmin)



class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ['clg_email','fname','lname','prn','mono1']

admin.site.register(StudentProfile,StudentProfileAdmin)