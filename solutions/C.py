from django.db.models import Model, QuerySet


def get_my_attempts(Attempt: Model) -> QuerySet:
    username = 'admin'
    return Attempt.objects.filter(user__username=username)
