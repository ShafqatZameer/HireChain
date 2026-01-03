from django.core.management.base import BaseCommand
from jobs.models import Job


class Command(BaseCommand):
    help = 'Populate database with sample job postings'

    def handle(self, *args, **kwargs):
        sample_jobs = [
            {
                'title': 'Software Specialist',
                'company_name': 'Innovate Corp',
                'location': 'Ill York, NY',
                'description': 'Lorem ipsum be the bonware blerching os heeatainry or uodone lorab amd esanalime ui dore tell, ti et cinerise ta fertse fantas. Planieso to or tneatiso, cut blunecn and fam la consafala a nireran and debue thesthy aute bons bote wn the aufpisture d saring the the spohalited a me the instelis and specilalie.',
                'requirements': 'Bachelor\'s degree in Computer Science or related field\n3+ years of software development experience\nProficiency in modern programming languages',
                'responsibilities': 'Design and develop software solutions\nCollaborate with cross-functional teams\nMaintain and improve existing codebases',
                'salary_range': '$80,000 - $120,000',
                'job_type': 'Full-time',
                'is_active': True,
            },
            {
                'title': 'Global Tech',
                'company_name': 'Global Tech',
                'location': 'Few York, NY',
                'description': 'Join our dynamic team as we build the future of technology. We are looking for passionate individuals who want to make a difference.',
                'requirements': 'Strong problem-solving skills\nExcellent communication abilities\nTeam player with leadership potential',
                'responsibilities': 'Lead technical projects\nMentor junior developers\nDrive innovation',
                'salary_range': '$90,000 - $140,000',
                'job_type': 'Full-time',
                'is_active': True,
            },
            {
                'title': 'Project Manager',
                'company_name': 'Creative Solutions',
                'location': 'London, UK',
                'description': 'We are seeking an experienced Project Manager to oversee multiple client projects and ensure successful delivery.',
                'requirements': 'PMP certification preferred\n5+ years project management experience\nExcellent organizational skills',
                'responsibilities': 'Manage project timelines and budgets\nCoordinate with stakeholders\nEnsure quality deliverables',
                'salary_range': '£60,000 - £85,000',
                'job_type': 'Full-time',
                'is_active': True,
            },
            {
                'title': 'Marketing Specialist',
                'company_name': 'Innovate Corp',
                'location': 'Remote',
                'description': 'Drive our marketing initiatives and help us reach new heights. Perfect for creative minds who love data-driven strategies.',
                'requirements': 'Marketing degree or equivalent experience\nSocial media expertise\nAnalytical mindset',
                'responsibilities': 'Develop marketing campaigns\nAnalyze market trends\nManage social media presence',
                'salary_range': '$55,000 - $75,000',
                'job_type': 'Full-time',
                'is_active': True,
            },
        ]

        created_count = 0
        for job_data in sample_jobs:
            job, created = Job.objects.get_or_create(
                title=job_data['title'],
                company_name=job_data['company_name'],
                defaults=job_data
            )
            if created:
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'Created job: {job.title} at {job.company_name}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Job already exists: {job.title} at {job.company_name}')
                )

        self.stdout.write(
            self.style.SUCCESS(f'\nSuccessfully created {created_count} new job posting(s)')
        )
