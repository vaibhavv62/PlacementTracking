from django.urls import path

from student_register import views

urlpatterns = [
    path('li/', views.student_list),
    path('fo/', views.student_form),
    path('reg/', views.student_reg),
    path('reg2/', views.student_reg2),
    path('reg3/', views.student_reg3),
    path('de/', views.student_delete),
    path('login/', views.student_login),
    path('allJobs/', views.all_jobs),
]