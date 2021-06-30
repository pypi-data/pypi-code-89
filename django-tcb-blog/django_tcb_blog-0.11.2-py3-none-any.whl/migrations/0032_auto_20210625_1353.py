# Generated by Django 3.1.2 on 2021-06-25 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0031_comment_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='entryenvelope',
            name='future_publish_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='entryenvelope',
            name='future_publish_processed_on',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='entryenvelope',
            name='should_publish_in_future',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entryenvelope',
            name='user_requested_future_publish',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
