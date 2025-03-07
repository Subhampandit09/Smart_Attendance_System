from django.urls import re_path
from . import views


urlpatterns=[
    re_path(r'^$', views.login, name='login'),
    re_path('^dashboard/$', views.dashboard, name='dashboard'),
    re_path('^dashboard/addstudent/$', views.add_student, name='addstudent'),
    re_path('^dashboard/train/$', views.train_database, name='train'),
    re_path('^dashboard/takeattendance/$', views.take_attendance, name='takeattendance'),
    re_path('^dashboard/view/', views.view_attendance, name='view'),
    re_path('^dashboard/settings/', views.settings, name='settings'),
    re_path('^dashboard/sendmail/', views.send_mail, name='sendmail'),
    re_path('^dashboard/profile/$', views.profile, name='profile'),
    re_path('^logout/$', views.logout, name='logout'),

    re_path(r'^api/chart/data/$', views.ChartData.as_view()),
]