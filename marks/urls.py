from django.urls import path
from . import views

urlpatterns = [

    path('add/', views.add_marks),

    path('list/', views.marks_list),

]