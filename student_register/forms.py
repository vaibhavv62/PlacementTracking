from django import forms

from student_register.models import Student,StudentProfile


class StudentForm(forms.ModelForm):
    class Meta():
        model = Student
        fields = '__all__'
        labels = {
            'name': 'Full Name',
            'email': 'Email ID',
            "rn": "Roll Number",
            "div": "Division",
            'branch': 'Branch',
            'mobile': 'Mobile Number',
            'sscm': 'SSC Marks',
            'hscm': 'HSC/Diploma Marks',
            'fe_cgpa': 'F.E. CGPA',
            'se_cgpa': 'S.E. CGPA',
            'te_cgpa': 'T.E. CGPA'
        }

class StudentProfileForm(forms.ModelForm):
    class Meta():
        model = StudentProfile
        fields = '__all__'
