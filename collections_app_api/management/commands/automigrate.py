from django.core.management import call_command
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Automates database migrations'

    def handle(self, *args, **kwargs):
        self.stdout.write('Auto running makemigrations...')
        call_command('makemigrations')
        self.stdout.write('Auto running migrate...')
        call_command('migrate')
        self.stdout.write('automigrate.py successful!')
