from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse, FileResponse
from jobs.models import Job
from .models import Application
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
        new_status = request.POST.get('status')
        
        if new_status in dict(Application.STATUS_CHOICES):
            application.status = new_status
            application.save()
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
