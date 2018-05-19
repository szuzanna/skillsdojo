from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('questionnaire', views.questionnaire, name='questionnaire'),
    path('courses', views.courses, name='courses'),
]
