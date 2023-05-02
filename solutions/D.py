from django.db.models import Model


def get_solved_count(Attempt: Model, Problem: Model) -> int:
    problem = Problem.objects.last()
    return Attempt.objects.filter(
        problem=problem,
        verdict=1,
    ).values('user').distinct().count()
