from django.db.models import Model, Q, QuerySet, Count


def get_users(User: Model) -> QuerySet:
    return User.objects.annotate(
        solved=Count('attempts__problem_id',
                     filter=Q(attempts__verdict=1), distinct=True)
    ).order_by('-solved', 'id')
