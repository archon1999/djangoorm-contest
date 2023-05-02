# Generated by Django 4.0.4 on 2023-05-02 08:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_remove_attempt_source_code'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attempt',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='problem',
            options={'ordering': ['id']},
        ),
        migrations.RemoveField(
            model_name='problem',
            name='author',
        ),
        migrations.RemoveField(
            model_name='problem',
            name='uid',
        ),
        migrations.RemoveField(
            model_name='user',
            name='uid',
        ),
    ]
