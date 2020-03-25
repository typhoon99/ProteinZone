from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('protein/',views.protein,name='protein'),
    path('creatine/',views.creatine,name='creatine'),
    path('peanutButter/',views.peanutButter,name='peanutButter'),
    path('preWorkout/',views.preWorkout,name='preWorkout'),
    path('bcaa/',views.bcaa,name='bcaa'),
    path('about/',views.about,name='about'),
    path('mailUs/',views.mailUs,name='mailUs'),
]
