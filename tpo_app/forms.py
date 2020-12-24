from .models import Jobs
from django import forms

class JobsModelForm(forms.ModelForm):
    class Meta:
        model = Jobs
        fields = '__all__'
        labels = {
            'company':'Name of the Organization',
            'job_pos': 'Job Position',
            'job_loc': 'Job Location',
            'ctc_offered':'CTC Offered',
            'service_agg':'ServiceAggrementInYrs',
            'date_of_joining':'Joining Date',
            'skills_req':'Skills Required',
            'selection_proc':'Selection Procedure',
            'date_of_campus':'Campus Date',
            'campus_venue':'campus Venue',
            'age':'Maximum Age',
            'passing_yr':'Passing Year',
            'xth_percentage':'Min. xth_percentage',
            'xiith_percentage':'Min. xiith_percentage',
            'diploma_percentage':'Min. diploma_percentage',
            'engg_cgpa':'Min. engg_cgpa'

        }