from django.urls import path
from . import views

urlpatterns = [
    path('', views.holi_finder, name='holi-finder'),
    path('holidays_result/', views.holidays_result, name='holidays_result'),
]
