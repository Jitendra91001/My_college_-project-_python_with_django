from django.urls import path
from . import views


urlpatterns=[
    path('',views.home),
    path('home/',views.home),
    path('index/',views.index),
    path('about/',views.about),
    path('contactus/',views.contactus),
    path('placements/',views.placement),
    path('adminlogin/',views.adminlogin),
    path('course/',views.course),
    path('ourcourses/',views.ourcourses),
    path('gallery/',views.imagegallery),
    path('recruiters/',views.recruiters)

]