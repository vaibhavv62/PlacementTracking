from . import views
from django.urls import path

urlpatterns = [
    path('login/',views.tpo_login,name='tpo_login'),
    path('logout/',views.tpo_logout,name='tpo_logout'),
    path('allstu/',views.all_students,name='allstu'),
    path('stufullprof/',views.student_full_profile,name='stu_full_prof'),
    path('newjob/',views.post_new_job,name='new_job'),
    path('vis/',views.visualize,name='visualize'),
]