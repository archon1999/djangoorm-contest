from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    uid = models.IntegerField()


class Problem(models.Model):
    class Ball(models.IntegerChoices):
        BEGINNER = 10
        BASIC = 30
        NORMAL = 70
        MEDIUM = 150
        ADVANCED = 400
        HARD = 1000
        EXTREMAL = 2500

    class Difficulty(models.IntegerChoices):
        BEGINNER = 1
        BASIC = 2
        NORMAL = 3
        MEDIUM = 4
        ADVANCED = 5
        HARD = 6
        EXTREMAL = 7

    uid = models.IntegerField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    time_limit = models.PositiveIntegerField(default=1000)
    memory_limit = models.PositiveIntegerField(default=256)
    title = models.CharField(max_length=255)
    body = models.TextField()
    difficulty = models.IntegerField(choices=Difficulty.choices)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    name = models.CharField(max_length=50)


class ProblemTag(models.Model):
    objects = models.Manager()
    problem = models.ForeignKey(
        Problem,
        on_delete=models.CASCADE,
        related_name='tags'
    )
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)


class Attempt(models.Model):
    class Verdict(models.IntegerChoices):
        IN_QUEUE = -2
        RUNNING = -1
        JUDGEMENT_FAILED = 0
        ACCEPTED = 1
        WRONG_ANSWER = 2
        TIME_LIMIT_EXCEEDED = 3
        RUNTIME_ERROR = 4
        OUTPUT_FORMAT_ERROR = 5
        MEMORY_LIMIT_EXCEEDED = 6
        REJECTED = 7
        COMPILATION_ERROR = 8
        COMMAND_EXECUTING_ERROR = 9
        IDLENESS_LIMIT_EXCEEDED = 10
        SYNTAX_ERROR = 11
        CHECKER_NOT_FOUND = 12
        ONLY_PYTHON = 13
        OBJECT_NOT_FOUND = 14
        FAKE_ACCEPTED = 15
        PARTIAL_SOLUTION = 16
        NOT_AVAILABLE_LANGUAGE = 17

    class Lang(models.TextChoices):
        PYTHON = 'py'
        CPP = 'cpp'
        R = 'r'
        HASKELL = 'hs'
        KOTLIN = 'kt'
        C = 'c'
        TEXT = 'text'
        KEP = 'kep'

    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='attempts',
        null=True,
        blank=True,
    )
    problem = models.ForeignKey(
        to=Problem,
        on_delete=models.CASCADE,
        related_name='attempts',
    )
    verdict = models.IntegerField(
        choices=Verdict.choices,
        default=Verdict.IN_QUEUE,
    )
    lang = models.CharField(
        max_length=10,
        choices=Lang.choices,
    )
    test_case_number = models.IntegerField(default=1, null=True)
    time = models.PositiveIntegerField(default=0)
    memory = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
