from django.core.management import call_command
from django.contrib.auth.models import User

def create_super_user():
    # Check if the superuser already exists
    if not User.objects.filter(username='admin').exists():
        call_command('createsuperuser', interactive=False, username='admin', email='admin@example.com', password='admin')
        print('Superuser created successfully.')
    else:
        print('Superuser already exists.')

if __name__ == '__main__':
    create_super_user()
