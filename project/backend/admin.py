from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Problem, Attempt, User


@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'difficulty']


@admin.register(Attempt)
class AttemptAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'problem', 'created', 'verdict']


@admin.register(User)
class UserAdmin(UserAdmin):
    pass
