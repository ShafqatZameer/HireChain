from django.urls import path
from . import views

app_name = 'applications'

urlpatterns = [
    path('apply/<int:job_id>/', views.apply_job_view, name='apply_job'),
    path('admin/applications/', views.admin_applications_view, name='admin_applications'),
    path('api/application/<int:application_id>/', views.application_detail_api, name='application_detail_api'),
    path('api/application/<int:application_id>/update-status/', views.update_application_status, name='update_status'),
    path('api/notifications/', views.get_notifications, name='get_notifications'),
    path('api/notifications/<int:notification_id>/read/', views.mark_notification_read, name='mark_notification_read'),
    path('api/notifications/read-all/', views.mark_all_notifications_read, name='mark_all_notifications_read'),
]
