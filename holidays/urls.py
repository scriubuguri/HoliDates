from django.urls import path
from . import views

urlpatterns = [
    path('', views.holidays, name="holidays"),
    path('holiday-result/', views.holidays_result, name="holiday-result")
]
