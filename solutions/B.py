from django.db.models import Model


def get_attempts_count(Attempt: Model, Problem: Model) -> int:
    problem = Problem.objects.first()
    return Attempt.objects.filter(problem_id=problem).count()
