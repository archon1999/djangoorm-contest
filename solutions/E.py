from django.db.models import Model, Count, Sum


def get_solved_tags_count(Attempt: Model) -> int:
    username = 'admin'
    return Attempt.objects.filter(
        user__username=username,
        verdict=1
    ).values('problem').order_by('problem').distinct().annotate(
        tags_count=Count('problem__tags', distinct=True)
    ).aggregate(
        sum_tags=Sum('tags_count'),
    )['sum_tags']
