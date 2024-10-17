from django.urls import path
from . import views

from .views import TutorListView, TutorView

urlpatterns = [
    path("tutors/",TutorListView.as_view(),name = 'tutor_list'),
    path("tut/<int:pk>/",TutorView.as_view(),name='tutor_single'),
    path('change_times/',views.change_times, name="change_times" )
]