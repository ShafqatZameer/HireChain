from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Job
from .forms import JobForm


def home_view(request):
    """
    Display all active jobs on home page.
    Follows Single Responsibility Principle - only handles home page display.
    """
    jobs = Job.objects.filter(is_active=True)
    return render(request, 'home.html', {'jobs': jobs})


def job_detail_api(request, job_id):
    """
    API endpoint to get job details for modal.
    Follows Interface Segregation Principle - specific API for job details.
    """
    job = get_object_or_404(Job, id=job_id, is_active=True)
    data = {
        'id': job.id,
        'title': job.title,
        'company': job.company_name,
        'location': job.location,
        'description': job.description,
        'requirements': job.requirements,
        'responsibilities': job.responsibilities,
        'salary_range': job.salary_range,
        'job_type': job.job_type,
        'posted_date': job.posted_date.strftime('%B %d, %Y'),
    }
    return JsonResponse(data)


@login_required
def create_job_view(request):
    """
    Handle job creation (admin only).
    Follows Single Responsibility Principle - only handles job creation.
    """
    if not request.user.is_admin_user():
        return render(request, '403.html', status=403)
    
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True, 'message': 'Job posted successfully!'})
        else:
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)
    
    form = JobForm()
    return render(request, 'jobs/create_job.html', {'form': form})
