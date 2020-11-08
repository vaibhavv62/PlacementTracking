import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect

from tpo_app.models import Jobs
from .models import StudentProfile

# Create your views here.
from student_register.forms import StudentForm, StudentProfileForm


def student_list(request):
    stuProfs = StudentProfile.objects.all()
    print(stuProfs)
    # u = request.user
    return render(request,"student_register/studentlist.html",{'user':stuProfs})
    # return HttpResponse("Hello, {}".format(stuProfs.all()))


def student_form(request):
    form = StudentForm
    return render(request,"student_register/studentform.html", {'form':form})

def student_reg(request):
    if request.method == "GET":
        print("GET req for student reg form, opening studentregform.html")
        return render(request,"student_register/studentregform.html")
    if request.method == "POST":
        print("POST req for student reg form, redirecting to view student_reg2()")
        # print(request.POST)
        # return redirect(student_reg2(request))
        request.session['form1'] = request.POST
        return redirect('/stu/reg2/')

def student_reg2(request):
    if request.method == "GET":
        print("GET req for student reg form2, opening studentregform2.html")
        print(request.GET)
        form1_data = request.session['form1']
        # print(type(form1_data),form1_data)
        # clgid = form1_data['clgid']
        return render(request,"student_register/studentregform2.html")
    if request.method == "POST":
        print("POST req for student reg form2, redirecting to view student_reg3()")
        request.session['form2'] = request.POST
        return redirect('/stu/reg3/')

def student_reg3(request):
    if request.method == "GET":
        print("GET req for student reg form3, opening studentregform3.html")
        print(request.GET)
        form1_data = request.session['form1']
        # print("form1:",type(form1_data), form1_data)
        form2_data = request.session['form2']
        # print("form2:",type(form2_data), form2_data)
        return render(request, "student_register/studentregform3.html")
    if request.method == "POST":
        print("POST req for student reg form3, Done")
        request.session['form3'] = request.POST

        form1_data = request.session['form1']
        # print("form1:", type(form1_data), form1_data)

        clgid = form1_data['clgid']
        # print(type(clgid))
        personal_email = form1_data['personal_email']
        parent_email = form1_data['parent_email']
        aadhar_no = form1_data['aadhar_no']
        fname = form1_data['fname']
        mname = form1_data['mname']
        lname = form1_data['lname']
        clg = form1_data['clg']
        prn = form1_data['prn']
        branch = form1_data['branch']
        gender = form1_data['gender']
        np = form1_data['np']
        dob = form1_data['dob']
        mt = form1_data['mt']
        other_lang = form1_data['other_lang']
        mono1 = form1_data['mono1']
        mono2 = form1_data['mono2']
        parent_mono1 = form1_data['parent_mono1']
        parent_mono2 = form1_data['parent_mono2']
        print('\nform1 data:',clgid, personal_email, parent_email, aadhar_no, fname, mname, lname, clg,
              prn, branch, gender, np, dob, mt, other_lang, mono1, mono2, parent_mono1, parent_mono2)

        form2_data = request.session['form2']
        # print("form2:", type(form2_data), form2_data)

        xth_board = form2_data['xth_board']
        # print(type(xth_board))
        xth_passing_yr = form2_data['xth_passing_yr']
        xth_marks_obtained = form2_data['xth_marks_obtained']
        xth_marks_outoff = form2_data['xth_marks_outoff']
        xiith_board = form2_data['xiith_board']
        xiith_passing_yr = form2_data['xiith_passing_yr']
        xiith_marks_obtained = form2_data['xiith_marks_obtained']
        xiith_marks_outoff = form2_data['xiith_marks_outoff']
        diploma_clg = form2_data['diploma_clg']
        diploma_passing_yr = form2_data['diploma_passing_yr']
        diploma_marks_obtained = form2_data['diploma_marks_obtained']
        diploma_marks_outoff = form2_data['diploma_marks_outoff']
        print('\nform2 data:',xth_board,xth_passing_yr,xth_marks_obtained,xth_marks_outoff,xiith_board,xiith_passing_yr,
              xiith_marks_obtained,xiith_marks_outoff,diploma_clg,diploma_passing_yr,
              diploma_marks_obtained,diploma_marks_outoff)

        form3_data = request.session['form3']
        # print("form3:", type(form3_data), form3_data)

        fe1_tot_credits_obtained = form3_data['fe1_tot_credits_obtained']
        # print(type(fe1_tot_credits_obtained))
        fe1_tot_credits = form3_data['fe1_tot_credits']
        fe1_cgpa = form3_data['fe1_cgpa']
        fe2_tot_credits_obtained = form3_data['fe2_tot_credits_obtained']
        fe2_tot_credits = form3_data['fe2_tot_credits']
        fe2_cgpa = form3_data['fe2_cgpa']
        se1_tot_credits_obtained = form3_data['se1_tot_credits_obtained']
        se1_tot_credits = form3_data['se1_tot_credits']
        se1_cgpa = form3_data['se1_cgpa']
        se2_tot_credits_obtained = form3_data['se2_tot_credits_obtained']
        se2_tot_credits = form3_data['se2_tot_credits']
        se2_cgpa = form3_data['se2_cgpa']
        te1_tot_credits_obtained = form3_data['te1_tot_credits_obtained']
        te1_tot_credits = form3_data['te1_tot_credits']
        te1_cgpa = form3_data['te1_cgpa']
        te2_tot_credits_obtained = form3_data['te2_tot_credits_obtained']
        te2_tot_credits = form3_data['te2_tot_credits']
        te2_cgpa = form3_data['te2_cgpa']
        be1_tot_credits_obtained = form3_data['be1_tot_credits_obtained']
        be1_tot_credits = form3_data['be1_tot_credits']
        be1_cgpa = form3_data['be1_cgpa']
        be2_tot_credits_obtained = form3_data['be2_tot_credits_obtained']
        be2_tot_credits = form3_data['be2_tot_credits']
        be2_cgpa = form3_data['be2_cgpa']
        engg_cgpa = (fe1_cgpa + fe2_cgpa + se1_cgpa + se2_cgpa + te1_cgpa + te2_cgpa + be1_cgpa + be2_cgpa) / 8
        if be2_cgpa==-1:
            engg_cgpa = ( fe1_cgpa + fe2_cgpa + se1_cgpa + se2_cgpa + te1_cgpa + te2_cgpa + be1_cgpa ) / 7
        elif be2_cgpa==-1 and be1_cgpa==-1:
            engg_cgpa = ( fe1_cgpa + fe2_cgpa + se1_cgpa + se2_cgpa + te1_cgpa + te2_cgpa ) / 6
        elif be2_cgpa==-1 and be1_cgpa==-1 and te2_cgpa==-1:
            engg_cgpa = ( fe1_cgpa + fe2_cgpa + se1_cgpa + se2_cgpa + te1_cgpa ) / 5
        no_of_dead_kt = form3_data['no_of_dead_kt']
        no_of_live_kt = form3_data['no_of_live_kt']
        no_of_yd_engg = form3_data['no_of_yd_engg']
        no_of_yd_diploma = form3_data['no_of_yd_diploma']
        no_of_yg = form3_data['no_of_yg']
        plan_after_engg = form3_data['plan_after_engg']
        te_mini_proj_company = form3_data['te_mini_proj_company']
        te_mini_proj_title = form3_data['te_mini_proj_title']
        certification1 = form3_data['certification1']
        certification2 = form3_data['certification2']
        AddOnCourse1 = form3_data['AddOnCourse1']
        AddOnCourse2 = form3_data['AddOnCourse2']
        print('\nform3 data:',fe1_tot_credits_obtained,fe1_tot_credits,fe1_cgpa,fe2_tot_credits_obtained,fe2_tot_credits,fe2_cgpa,
              se1_tot_credits_obtained,se1_tot_credits,se1_cgpa,se2_tot_credits_obtained,se2_tot_credits,se2_cgpa,
              te1_tot_credits_obtained,te1_tot_credits,te1_cgpa,te2_tot_credits_obtained,te2_tot_credits,te2_cgpa,
              be1_tot_credits_obtained,be1_tot_credits,be1_cgpa,be2_tot_credits_obtained,be2_tot_credits,be2_cgpa,
              engg_cgpa,no_of_dead_kt,no_of_live_kt,no_of_yd_engg,no_of_yd_diploma,no_of_yg,plan_after_engg,
              te_mini_proj_company,te_mini_proj_title,certification1,certification2,AddOnCourse1,AddOnCourse2)

        print('Saving the student profile data into database....')
        s = StudentProfile()
        s.clg_email = clgid
        s.personal_email = personal_email
        s.parent_email = parent_email
        s.aadhar_no = aadhar_no
        s.fname = fname
        s.mname = mname
        s.lname = lname
        s.clg = clg
        s.prn = prn
        s.branch = branch
        s.gender = gender
        s.native_place = np
        # s.dob = dob
        s.dob = '1998-08-26'
        s.mother_tounge = mt
        s.other_lang = other_lang
        s.mono1 = mono1
        s.mono2 = mono2
        s.parent_mono1 = parent_mono1
        s.parent_mono2 = parent_mono2
        s.xth_board = xth_board
        s.xth_passing_yr = xth_passing_yr
        s.xth_marks_obtained = xth_marks_obtained
        s.xth_marks_outoff = xth_marks_outoff
        s.xiith_board = xiith_board
        s.xiith_passing_yr = xiith_passing_yr
        s.xiith_marks_obtained = xiith_marks_obtained
        s.xiith_marks_outoff = xiith_marks_outoff
        s.diploma_clg = diploma_clg
        s.diploma_passing_yr = diploma_passing_yr
        s.diploma_marks_obtained = diploma_marks_obtained
        s.diploma_marks_outoff = diploma_marks_outoff
        s.fe1_tot_credits_obtained = fe1_tot_credits_obtained
        s.fe1_tot_credits = fe1_tot_credits
        s.fe1_cgpa = fe1_cgpa
        s.fe2_tot_credits_obtained = fe2_tot_credits_obtained
        s.fe2_tot_credits = fe2_tot_credits
        s.fe2_cgpa = fe2_cgpa
        s.se1_tot_credits_obtained = se1_tot_credits_obtained
        s.se1_tot_credits = se1_tot_credits
        s.se1_cgpa = se1_cgpa
        s.se2_tot_credits_obtained = se2_tot_credits_obtained
        s.se2_tot_credits  = se2_tot_credits
        s.se2_cgpa = se2_cgpa
        s.te1_tot_credits_obtained = te1_tot_credits_obtained
        s.te1_tot_credits = te1_tot_credits
        s.te1_cgpa = te1_cgpa
        s.te2_tot_credits_obtained = te2_tot_credits_obtained
        s.te2_tot_credits = te2_tot_credits
        s.te2_cgpa = te2_cgpa
        s.be1_tot_credits_obtained = be1_tot_credits_obtained
        s.be1_tot_credits = be1_tot_credits
        s.be1_cgpa = be1_cgpa
        s.be2_tot_credits_obtained = be2_tot_credits_obtained
        s.be2_tot_credits = be2_tot_credits
        s.be2_cgpa = be2_cgpa
        s.engg_cgpa = engg_cgpa
        s.no_of_dead_kt = no_of_dead_kt
        s.no_of_live_kt = no_of_live_kt
        s.no_of_yd_engg = no_of_yd_engg
        s.no_of_yd_diploma = no_of_yd_diploma
        s.no_of_yg = no_of_yg
        s.plan_after_engg = plan_after_engg
        s.te_mini_proj_company = te_mini_proj_company
        s.te_mini_proj_title = te_mini_proj_title
        s.certification1 = certification1
        s.certification2 = certification2
        s.AddOnCourse1 = AddOnCourse1
        s.AddOnCourse2 = AddOnCourse2

        print(s,type(s))
        s.save()
        return HttpResponse("Done")

def student_delete(request):
    if request.method == "GET":
        print("GET request method for student_delete")

        jobs = Jobs.objects.all()
        # date = datetime.datetime.now()
        date = datetime.date.today()
        # date2 = job.date_of_campus
        date2 = request.session['date2']
        print(date, type(date),'\n',date2,type(date2))
        # di = jobs.__dict__
        context = {'jobs': jobs, 'current_date': date,'campus_date':date2}
        template_name = "student_register/try.html"
        return render(request, template_name, context)
    else:
        print("POST request method for student_delete")
        dt = request.POST['date_of_campus']
        # pw = request.POST['pw']
        request.session['date2'] = dt
        print(f"Data got from frontend is {dt}")
        return HttpResponse(f"{dt}")


def student_login(request):
    if request.method == "GET":
        print("GET request method for login page")
        dt = datetime.datetime.now()
        # print(dt, type(dt))
        context = {"dt":dt}
        template_name = "student_register/index.html"
        return render(request, template_name, context)
    else:
        print("POST request method for login page")
        un = request.POST['un']
        pw = request.POST['pw']
        print(f"Data got from frontend is {un} and {pw}")
        return HttpResponse(f"{un} you are Logged In!")

def all_jobs(request):
    print("GET request method for all_jobs")
    jobs = Jobs.objects.all()
    # date = datetime.datetime.now()
    date = datetime.date.today()
    # date2 = job.date_of_campus
    print(date,type(date))
    # di = jobs.__dict__
    context = {'jobs':jobs,'current_date':date}
    template_name = "student_register/allJobs.html"
    return render(request, template_name, context)



