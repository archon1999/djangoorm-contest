import os
import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'core.settings'
django.setup()

from backend.models import Problem, Attempt, User, Tag

import random
print(Problem.objects.first())

tags = list(Tag.objects.all().values_list('id', flat=True))
for problem in Problem.objects.all():
    for _ in range(random.randint(0, 4)):
        problem.tags.create(tag_id=random.choice(tags))
