from django.db import models
from django.conf import settings
from jobs.models import Job


class Application(models.Model):
    """
    Application model to store job applications.
    Follows Single Responsibility Principle - handles application data.
    """
    STATUS_CHOICES = (
        ('new', 'New'),
        ('reviewing', 'Reviewing'),
        ('interview_scheduled', 'Interview Scheduled'),
        ('rejected', 'Rejected'),
    )
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='applications')
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    linkedin = models.URLField(blank=True, null=True)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    portfolio = models.URLField(blank=True, null=True)
    cover_letter = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='new')
    applied_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'applications'
        ordering = ['-applied_date']
        unique_together = ('user', 'job')
        verbose_name = 'Application'
        verbose_name_plural = 'Applications'
    
    def __str__(self):
        return f"{self.full_name} - {self.job.title}"
    
    def get_status_badge_class(self):
        """Get CSS class for status badge"""
        status_classes = {
            'new': 'badge-new',
            'reviewing': 'badge-reviewing',
            'interview_scheduled': 'badge-interview',
            'rejected': 'badge-rejected',
        }
        return status_classes.get(self.status, 'badge-default')
