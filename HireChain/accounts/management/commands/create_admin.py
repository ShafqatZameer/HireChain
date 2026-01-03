from django.core.management.base import BaseCommand
from accounts.models import CustomUser


class Command(BaseCommand):
    help = 'Creates the default admin user'

    def handle(self, *args, **options):
        username = 'Admin123'
        email = 'admin@hirechain.com'
        password = 'hirechain123'
        
        # Check if user already exists
        if CustomUser.objects.filter(username=username).exists():
            self.stdout.write(self.style.WARNING(f'User "{username}" already exists.'))
            return
        
        # Create superuser
        user = CustomUser.objects.create_superuser(
            username=username,
            email=email,
            password=password,
            user_type='admin'
        )
        
        self.stdout.write(self.style.SUCCESS(f'Successfully created admin user "{username}"'))
        self.stdout.write(self.style.SUCCESS(f'Username: {username}'))
        self.stdout.write(self.style.SUCCESS(f'Password: {password}'))
