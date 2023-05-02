from collections import Counter
from django.db.models import Model


def get_max_solved_user(Attempt: Model) -> str:
    return Counter(
        Attempt.objects.filter(
            verdict=1
        ).order_by(
            'problem', 'user'
        ).distinct().values_list(
            'user__username', flat=True
        )
    ).most_common(1)[0][0]
