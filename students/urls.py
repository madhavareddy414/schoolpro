from django.conf.urls import url
from django.urls import path

import appviewwithser
from appviewwithser.views import StudView
from students.views import studentslist, register, totalstudents, search, delete

urlpatterns = [
    path('',studentslist),
    path('reg/',register),
    path('all/',totalstudents),
    path('find/',search),
    path('del/',delete),
    url(r'appvser', StudView.as_view()),

]