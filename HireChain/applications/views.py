from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse, FileResponse
from jobs.models import Job
from .models import Application, Notification
from .forms import ApplicationForm


@login_required
def apply_job_view(request, job_id):
    """
    Handle job application submission.
    Follows Single Responsibility Principle - only handles application creation.
    """
    job = get_object_or_404(Job, id=job_id, is_active=True)
    
    # Check if user already applied
    if Application.objects.filter(user=request.user, job=job).exists():
        return JsonResponse({
            'success': False, 
            'message': 'You have already applied for this job.'
        }, status=400)
    
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user
            application.job = job
            application.save()
            
            # Create notification for application submission
            Notification.objects.create(
                user=request.user,
                application=application,
                message=f"Your application for {job.title} at {job.company_name} has been submitted successfully!"
            )
            
            return JsonResponse({
                'success': True, 
                'message': 'Application submitted successfully!'
            })
        else:
            return JsonResponse({
                'success': False, 
                'errors': form.errors
            }, status=400)
    
    form = ApplicationForm(initial={
        'email': request.user.email,
        'full_name': request.user.get_full_name() or request.user.username,
        'phone': request.user.phone,
        'linkedin': request.user.linkedin,
    })
    return render(request, 'applications/apply.html', {'form': form, 'job': job})


@login_required
def admin_applications_view(request):
    """
    Display all applications for admin.
    Follows Single Responsibility Principle - only handles applications display.
    """
    if not request.user.is_admin_user():
        return render(request, '403.html', status=403)
    
    applications = Application.objects.select_related('user', 'job').all()
    
    # Filter by status if provided
    status_filter = request.GET.get('status')
    if status_filter:
        applications = applications.filter(status=status_filter)
    
    # Search functionality
    search_query = request.GET.get('search')
    if search_query:
        applications = applications.filter(full_name__icontains=search_query)
    
    return render(request, 'applications/admin_applications.html', {
        'applications': applications
    })


@login_required
def application_detail_api(request, application_id):
    """
    API endpoint to get application details.
    Follows Interface Segregation Principle - specific API for application details.
    """
    if not request.user.is_admin_user():
        return JsonResponse({'error': 'Unauthorized'}, status=403)
    
    application = get_object_or_404(Application, id=application_id)
    data = {
        'id': application.id,
        'full_name': application.full_name,
        'email': application.email,
        'phone': application.phone,
        'linkedin': application.linkedin,
        'portfolio': application.portfolio,
        'cover_letter': application.cover_letter,
        'status': application.status,
        'job_title': application.job.title,
        'applied_date': application.applied_date.strftime('%B %d, %Y'),
        'resume_url': application.resume.url if application.resume else None,
    }
    return JsonResponse(data)


@login_required
def update_application_status(request, application_id):
    """
    Update application status (admin only).
    Follows Single Responsibility Principle - only handles status updates.
    """
    if not request.user.is_admin_user():
        return JsonResponse({'error': 'Unauthorized'}, status=403)
    
    if request.method == 'POST':
        application = get_object_or_404(Application, id=application_id)
        old_status = application.status
        new_status = request.POST.get('status')
        
        if new_status in dict(Application.STATUS_CHOICES):
            application.status = new_status
            application.save()
            
            # Create notification for status change
            status_messages = {
                'new': 'Your application status has been updated to: New',
                'reviewing': f'Good news! Your application for {application.job.title} is now being reviewed by the hiring team.',
                'interview_scheduled': f'Congratulations! You have been selected for an interview for the {application.job.title} position. The HR team will contact you soon.',
                'rejected': f'Thank you for your interest in the {application.job.title} position. Unfortunately, we have decided to move forward with other candidates.'
            }
            
            # Only create notification if status actually changed
            if old_status != new_status:
                Notification.objects.create(
                    user=application.user,
                    application=application,
                    message=status_messages.get(new_status, f'Your application status has been updated to: {application.get_status_display()}')
                )
            
            return JsonResponse({
                'success': True, 
                'message': 'Status updated successfully!'
            })
        else:
            return JsonResponse({
                'success': False, 
                'message': 'Invalid status.'
            }, status=400)
    
    return JsonResponse({'error': 'Invalid request'}, status=400)

@login_required
def get_notifications(request):
    """Get user's unread notifications"""
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Unauthorized'}, status=401)
    
    notifications = Notification.objects.filter(
        user=request.user,
        is_read=False
    ).select_related('application__job').order_by('-created_at')[:10]
    
    notifications_data = [{
        'id': n.id,
        'message': n.message,
        'created_at': n.created_at.strftime('%b %d, %Y %I:%M %p'),
        'application_id': n.application.id,
        'job_title': n.application.job.title
    } for n in notifications]
    
    return JsonResponse({
        'notifications': notifications_data,
        'count': notifications.count()
    })

@login_required
def mark_notification_read(request, notification_id):
    """Mark a specific notification as read"""
    if request.method == 'POST':
        notification = get_object_or_404(Notification, id=notification_id, user=request.user)
        notification.is_read = True
        notification.save()
        return JsonResponse({'success': True})
    return JsonResponse({'error': 'Invalid request'}, status=400)

@login_required
def mark_all_notifications_read(request):
    """Mark all notifications as read"""
    if request.method == 'POST':
        Notification.objects.filter(user=request.user, is_read=False).update(is_read=True)
        return JsonResponse({'success': True})
    return JsonResponse({'error': 'Invalid request'}, status=400)
