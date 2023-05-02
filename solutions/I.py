from django.db.models import Model, QuerySet


def get_queryset(Attempt: Model) -> QuerySet:
    return Attempt.objects.all()[:100].select_related('user')
