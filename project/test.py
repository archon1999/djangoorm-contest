import os
import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'core.settings'
django.setup()

from backend.models import Problem

print(Problem.objects.first())
