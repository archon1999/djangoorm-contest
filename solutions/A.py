from django.db.models import Model, QuerySet


def get_problems(Problem: Model) -> QuerySet:
    return Problem.objects.all()[:10]
