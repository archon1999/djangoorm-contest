# Generated by Django 4.0.4 on 2023-05-02 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_user_uid'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='uid',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
