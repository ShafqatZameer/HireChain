from django.urls import path
from . import views

app_name = 'applications'

urlpatterns = [
    path('apply/<int:job_id>/', views.apply_job_view, name='apply_job'),
    path('admin/applications/', views.admin_applications_view, name='admin_applications'),
    path('api/application/<int:application_id>/', views.application_detail_api, name='application_detail_api'),
    path('api/application/<int:application_id>/update-status/', views.update_application_status, name='update_status'),
]
