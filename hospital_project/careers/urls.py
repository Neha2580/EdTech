from django.urls import path
from . import views

urlpatterns = [path('careers/', views.careers , name = 'careers'),]