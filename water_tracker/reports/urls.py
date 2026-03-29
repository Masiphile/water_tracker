from django.urls import path
from . import views

urlpatterns = [
    path('report/', views.report_leak, name='report'),
    path('success/', views.success, name='success'),
]