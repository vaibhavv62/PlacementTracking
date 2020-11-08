from django.http import HttpResponse
from django.shortcuts import render
import datetime

# Create your views here.
from student_register.models import StudentProfile
from tpo_app.models import Jobs


def tpo_login(request):
    dt = datetime.datetime.now()
    print(dt, type(dt))
    context = {"dt":dt}
    template_name = "tpo_app/tpoLogin.html"
    return render(request, template_name, context)

def all_students(request):
    students = StudentProfile.objects.all()
    context = {'students':students}
    template_name = "tpo_app/allStudents.html"
    return render(request, template_name, context)

def student_full_profile(request):
    student = StudentProfile.objects.get(prn='71717219J')
    di = student.__dict__
    di.pop('_state')
    context = {'stu':di}
    template_name = "tpo_app/studentFullProfile.html"
    return  render(request,template_name,context)

def post_new_job(request):
    # context = {}
    # template_name = "tpo_app/newJob.html"
    # return render(request,template_name,context)
    if request.method == "GET":
        print("GET req for post_new_job, opening tpo_app/newJob.html")
        # print(request.GET)
        context = {}
        template_name = "tpo_app/newJob.html"
        return render(request,template_name,context)
    if request.method == "POST":
        print("POST req for post_new_job",request.POST)
        print('Saving the student profile data into database....')
        j = Jobs()
        j.company = request.POST['company']
        j.reg_link = request.POST['reg_link']
        j.date_of_campus = request.POST['date_of_campus']
        j.campus_venue = request.POST['campus_venue']
        j.job_loc = request.POST['job_loc']
        j.job_pos = request.POST['job_pos']
        j.ctc_offered = request.POST['ctc_offered']
        j.service_agg = request.POST['service_agg']
        j.skills_req = request.POST['skills_req']
        j.selection_proc = request.POST['selection_proc']
        j.age = request.POST['age']
        j.passing_yr = request.POST['passing_yr']
        j.xth_percentage = request.POST['xth_percentage']
        j.xiith_percentage = request.POST['xiith_percentage']
        j.diploma_percentage = request.POST['diploma_percentage']
        j.engg_cgpa = request.POST['engg_cgpa']
        j.no_of_dead_kt = request.POST['no_of_dead_kt']
        j.no_of_live_kt = request.POST['no_of_live_kt']
        j.no_of_yg = request.POST['no_of_yg']
        j.date_of_joining = request.POST['date_of_joining']
        j.save()
        print("New job added in the database succesfully..")
        return HttpResponse("Done")


def visualize(request):
    # import pandas as pd
    # import matplotlib.pyplot as plt
    #
    # s = pd.Series([1, 2, 3])
    # fig, ax = plt.subplots()
    # s.plot.bar()
    # fig.savefig('static/images/my_plot1.png')
    cnt = 0
    import pandas as pd
    import matplotlib.pyplot as plt

    s = pd.Series([1, 2, 3])
    fig, ax = plt.subplots()
    s.plot.bar()
    # img = 'static/images/my_plot'+str(cnt)+'.png'
    # print(img)
    fig.savefig('static/images/my_plot3.png')

    feimg = 'images/my_plot'+str(cnt)+'.png'
    print(feimg)
    context = {'feimg':feimg}
    template_name = "tpo_app/visualize.html"
    cnt += 1
    return render(request,template_name,context)
