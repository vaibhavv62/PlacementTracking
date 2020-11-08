import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','PlacementTracking.settings')
import django
django.setup()
from student_register.models import StudentProfile

from faker import Faker
import random
faker = Faker('en_IN')

def populate_student(n):

    clgList = ['MMCOE','MMIT']
    branchList = ['Computer', 'Mechanical', 'IT', 'EnTC', 'Electrical']
    genderList = ['Male', 'Female']
    mtList = ['Assamese', 'Bengali', 'Bodo', 'Dogri', 'Gujarati', 'Hindi', 'Kannada', 'Kashmiri', 'Konkani', 'Maithili', 'Malayalam',
        'Manipuri', 'Marathi','Nepali', 'Oriya', 'Punjabi', 'Sanskrit', 'Santhali', 'Sindhi', 'Tamil', 'Telugu','Urdu']
    olList = ['Arabic','Chinese','Persian','French','German','Japanese','Russian','Spanish']
    mail_domain = ['@mmit.edu.in','@mmcoe.edu.in']
    mail_year = ['2015','2016','2017','2018','2019']
    mail_branch = ['.comp','.mech','.ele','.entc','.it']
    personal_mail_domain = ['@gmail.com','@yahoo.com', 'outlook.com']
    xth_boardList = ['State Board','CBSE','ICSE','Other']
    xiith_boardList = ['State Board','CBSE','ICSE','Other']
    xth_passing_yrList = [2012,2013,2014,2015]
    # xiith_passing_yrList = ['2014','2015','2016','2017']
    plan_after_enggList = ['Job','ME','Mtech','MBA','MS','Enterprenureship','MPSC','UPSC']
    projTitle = [' Portal', ' Mgmt Sys']
    certification1List = ['DevOps', 'Cybersecurity', 'Blockchain', 'Kubernetes', 'AWS']
    certification2List = ['Web Dev.','Data Science', 'Machine Learning',' AI', 'Data Analytics', 'Buisness Mgmt']
    AddOnCourse1List = ['DevOps Course', 'Cybersecurity Course', 'Blockchain Course', 'Kubernetes Course', 'AWS Course']
    AddOnCourse2List = ['Web Dev. Course','Data Science Course', 'Machine Learning Course',' AI Course',
                        'Data Analytics Course', 'Buisness Mgmt Course']


    for i in range(n):

        fname = faker.first_name()
        mname = faker.word()
        lname = faker.last_name()
        # clg_email = faker.email()
        clg_email = lname.lower() + fname.lower() + random.choice(mail_year) + random.choice(mail_branch) + random.choice(mail_domain)
        clg = random.choice(clgList)
        randomCapLetter = chr(random.randint(65,90))
        prn = str(faker.random_int(71111111,79999999)) + randomCapLetter
        branch = random.choice(branchList)
        dob = faker.date_of_birth()
        gender = random.choice(genderList)
        native_place = faker.city()
        mother_tounge = random.choice(mtList)
        other_lang = random.choice(olList)
        mono1 = faker.random_int(7111111111,9999999999)
        mono2 = faker.random_int(7111111111,9999999999)
        parent_mono1 = faker.random_int(7111111111,9999999999)
        parent_mono2 = faker.random_int(7111111111,9999999999)
        personal_email = fname.lower() + lname.lower() + str(random.randint(1,99)) + random.choice(personal_mail_domain)
        parent_email = faker.email()
        xth_board = random.choice(xth_boardList)
        xth_passing_yr = random.choice(xth_passing_yrList)
        xth_marks_obtained = random.randint(300,490)
        xth_marks_outoff = 500
        xth_percentage = (xth_marks_obtained / xth_marks_outoff) * 100
        xiith_board = random.choice(xiith_boardList)
        xiith_passing_yr = xth_passing_yr + 2
        xiith_marks_obtained = random.randint(350,490)
        xiith_marks_outoff = 650
        xiith_percentage = (xiith_marks_obtained / xiith_marks_outoff) * 100
        diploma_clg = faker.city() + ' University'
        diploma_passing_yr = xth_passing_yr + 3
        diploma_marks_obtained = random.randint(350,490)
        diploma_marks_outoff = 500
        diploma_percentage = (diploma_marks_obtained / diploma_marks_outoff) * 100
        fe1_tot_credits = 200
        fe1_tot_credits_obtained = random.randint(20,50)
        fe1_cgpa = fe1_tot_credits/fe1_tot_credits_obtained
        fe2_tot_credits = 200
        fe2_tot_credits_obtained = random.randint(20,50)
        fe2_cgpa = fe2_tot_credits/fe2_tot_credits_obtained
        se1_tot_credits = 200
        se1_tot_credits_obtained = random.randint(20,50)
        se1_cgpa = se1_tot_credits/se1_tot_credits_obtained
        se2_tot_credits = 200
        se2_tot_credits_obtained = random.randint(20,50)
        se2_cgpa = se2_tot_credits/se2_tot_credits_obtained
        te1_tot_credits = 200
        te1_tot_credits_obtained = random.randint(20,50)
        te1_cgpa = te1_tot_credits/te1_tot_credits_obtained
        te2_tot_credits = 200
        te2_tot_credits_obtained = random.randint(20,50)
        te2_cgpa = te2_tot_credits/te2_tot_credits_obtained
        be1_tot_credits = 200
        be1_tot_credits_obtained = random.randint(20,50)
        be1_cgpa = be1_tot_credits/be1_tot_credits_obtained
        be2_tot_credits = 200
        be2_tot_credits_obtained = random.randint(20,50)
        be2_cgpa = be2_tot_credits/be2_tot_credits_obtained

        engg_cgpa = (fe1_cgpa + fe2_cgpa + se1_cgpa + se2_cgpa + te1_cgpa + te2_cgpa + be1_cgpa + be2_cgpa) / 8
        if be2_cgpa == -1:
            engg_cgpa = (fe1_cgpa + fe2_cgpa + se1_cgpa + se2_cgpa + te1_cgpa + te2_cgpa + be1_cgpa) / 7
        elif be2_cgpa == -1 and be1_cgpa == -1:
            engg_cgpa = (fe1_cgpa + fe2_cgpa + se1_cgpa + se2_cgpa + te1_cgpa + te2_cgpa) / 6
        elif be2_cgpa == -1 and be1_cgpa == -1 and te2_cgpa == -1:
            engg_cgpa = (fe1_cgpa + fe2_cgpa + se1_cgpa + se2_cgpa + te1_cgpa) / 5

        no_of_dead_kt = random.randint(0,10)
        no_of_live_kt = random.randint(0,4)
        no_of_yd_engg = random.randint(0,3)
        no_of_yd_diploma = random.randint(0,3)
        no_of_yg = no_of_yd_engg + no_of_yd_diploma
        plan_after_engg = random.choice(plan_after_enggList)
        te_mini_proj_company = faker.company()
        te_mini_proj_title = faker.job() + random.choice(projTitle)
        certification1 = random.choice(certification1List)
        certification2 = random.choice(certification2List)
        AddOnCourse1 = random.choice(AddOnCourse1List)
        AddOnCourse2 = random.choice(AddOnCourse2List)
        aadhar_no = random.randint(666666666666,999999999999)
        print('\nGenerating fake Data.....')
        print('Data Generated as-\n')

        print(clg_email,fname,mname,lname,clg,prn,branch,dob,gender,native_place,mother_tounge,other_lang,mono1,mono2,
              parent_mono1,parent_mono2,personal_email,parent_email, xth_board, xth_passing_yr,
              xth_marks_obtained,xth_marks_outoff,xth_percentage,xiith_board, xiith_passing_yr,xiith_marks_obtained,
              xiith_marks_outoff, xiith_percentage,diploma_clg,diploma_passing_yr,diploma_marks_obtained,
              diploma_marks_outoff, diploma_percentage,fe1_tot_credits,fe1_tot_credits_obtained,fe1_cgpa,
              fe2_tot_credits,fe2_tot_credits_obtained,fe2_cgpa,se1_tot_credits,se1_tot_credits_obtained,se1_cgpa,
              se2_tot_credits,se2_tot_credits_obtained,se2_cgpa,be1_tot_credits,be1_tot_credits_obtained,be1_cgpa,
              be2_tot_credits,be2_tot_credits_obtained,be2_cgpa,engg_cgpa,no_of_dead_kt,no_of_live_kt,no_of_yd_engg,
              no_of_yd_diploma, no_of_yg, plan_after_engg, te_mini_proj_company, te_mini_proj_title, certification1, certification2,
              AddOnCourse1,AddOnCourse2, aadhar_no)

        print('\nGoing to add above record in database....')

        s = StudentProfile.objects.get_or_create(clg_email = clg_email,fname=fname,mname=mname,lname=lname,clg=clg,
                                                 prn = prn, branch = branch, dob = dob, gender = gender, native_place = native_place,
                                                 mother_tounge = mother_tounge, other_lang=other_lang, mono1=mono1, mono2=mono2,
                                                 parent_mono1=parent_mono1, parent_mono2=parent_mono2, personal_email=personal_email,
                                                 parent_email=parent_email,xth_board=xth_board,xth_passing_yr=xth_passing_yr,
                                                 xth_marks_obtained=xth_marks_obtained, xth_marks_outoff=xth_marks_outoff,
                                                 xth_percentage = xth_percentage,
                                                 xiith_board = xiith_board, xiith_passing_yr = xiith_passing_yr,
                                                 xiith_marks_obtained = xiith_marks_obtained, xiith_marks_outoff=xiith_marks_outoff,
                                                 xiith_percentage = xiith_percentage,
                                                 diploma_clg = diploma_clg, diploma_passing_yr = diploma_passing_yr,
                                                 diploma_marks_obtained = diploma_marks_obtained, diploma_marks_outoff = diploma_marks_outoff,
                                                 diploma_percentage = diploma_percentage,
                                                 fe1_tot_credits=fe1_tot_credits, fe1_tot_credits_obtained=fe1_tot_credits_obtained,
                                                 fe1_cgpa = fe1_cgpa,
                                                 fe2_tot_credits=fe2_tot_credits, fe2_tot_credits_obtained=fe2_tot_credits_obtained,
                                                 fe2_cgpa = fe2_cgpa,
                                                 se1_tot_credits=se1_tot_credits, se1_tot_credits_obtained=se1_tot_credits_obtained,
                                                 se1_cgpa = se1_cgpa,
                                                 se2_tot_credits=se2_tot_credits, se2_tot_credits_obtained=se2_tot_credits_obtained,
                                                 se2_cgpa = se2_cgpa,
                                                 te1_tot_credits=te1_tot_credits, te1_tot_credits_obtained=te1_tot_credits_obtained,
                                                 te1_cgpa = te1_cgpa,
                                                 te2_tot_credits=te2_tot_credits, te2_tot_credits_obtained=te2_tot_credits_obtained,
                                                 te2_cgpa = te2_cgpa,
                                                 be1_cgpa = be1_cgpa,
                                                 be1_tot_credits=be1_tot_credits, be1_tot_credits_obtained=be1_tot_credits_obtained,
                                                 be2_tot_credits=be2_tot_credits, be2_tot_credits_obtained=be2_tot_credits_obtained,
                                                 be2_cgpa = be2_cgpa,engg_cgpa = engg_cgpa,
                                                 no_of_dead_kt = no_of_dead_kt, no_of_live_kt= no_of_live_kt,
                                                 no_of_yd_engg = no_of_yd_engg, no_of_yd_diploma = no_of_yd_diploma,
                                                 no_of_yg = no_of_yg, plan_after_engg= plan_after_engg,
                                                 te_mini_proj_company = te_mini_proj_company, te_mini_proj_title= te_mini_proj_title,
                                                 certification1 = certification1, certification2 = certification2,
                                                 AddOnCourse1 = AddOnCourse1, AddOnCourse2 = AddOnCourse2, aadhar_no=aadhar_no
                                                 )

        print('Above record added in database Successfully!....')

populate_student(1)