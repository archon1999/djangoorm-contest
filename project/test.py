import os
import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'core.settings'
django.setup()

from backend.models import Problem, Attempt, User

print(Problem.objects.first())
