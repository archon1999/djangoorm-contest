import functools

from django.db import connection


def query_count(func):
    @functools.wraps(func)
    def inner_func(*args, **kwargs):
        start_queries = len(connection.queries)
        result = func(*args, **kwargs)
        end_queries = len(connection.queries)
        print(end_queries - start_queries)
        return result

    return inner_func
