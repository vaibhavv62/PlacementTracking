from django.urls import path

from student_register import views

urlpatterns = [
    path('li/', views.student_list,name='allstudents'),
    path('fo/', views.student_form),
    path('reg/', views.student_reg),
    path('reg2/', views.student_reg2),
    path('reg3/', views.student_reg3),
    path('de/', views.student_delete),
    path('login/', views.student_login,name='stulogin'),
    path('logout/',views.student_logout,name='stu_logout'),
    path('signup/', views.student_signupView,name='signup'),
    path('alljobs/', views.all_jobs,name='alljobs'),
]