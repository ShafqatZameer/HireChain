from django.db import models
from django.utils.text import slugify


class Job(models.Model):
    """
    Job model to store job postings.
    Follows Single Responsibility Principle - handles job posting data.
    """
    title = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.TextField()
    requirements = models.TextField(blank=True, null=True)
    responsibilities = models.TextField(blank=True, null=True)
    salary_range = models.CharField(max_length=100, blank=True, null=True)
    job_type = models.CharField(max_length=50, default='Full-time')
    is_active = models.BooleanField(default=True)
    posted_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, blank=True)
    
    class Meta:
        db_table = 'jobs'
        ordering = ['-posted_date']
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.title}-{self.company_name}")
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.title} at {self.company_name}"
    
    def get_short_description(self, length=150):
        """Get truncated description"""
        if len(self.description) > length:
            return self.description[:length] + "..."
        return self.description
