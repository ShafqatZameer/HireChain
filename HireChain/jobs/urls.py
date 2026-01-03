from django.urls import path
from . import views

app_name = 'jobs'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('api/job/<int:job_id>/', views.job_detail_api, name='job_detail_api'),
    path('create/', views.create_job_view, name='create_job'),
]
