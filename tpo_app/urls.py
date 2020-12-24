from . import views
from django.urls import path

urlpatterns = [
    path('login/',views.tpo_login_view,name='tpo_login'),
    path('logout/',views.tpo_logout_view,name='tpo_logout'),
    path('allstu/',views.all_students_view,name='allstu'),
    path('stufullprof/',views.student_full_profile_view,name='stu_full_prof'),
    path('newjob/',views.post_new_job_view,name='new_job'),
    path('updatejob/<int:id>',views.update_job_view,name='update_job'),
    path('deletejob/<int:id>',views.delete_job_view,name='delete_job'),
    path('vis/',views.visualize,name='visualize'),
]