# Generated by Django 3.1 on 2020-09-25 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0003_auto_20200915_1839'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='offer_description',
            field=models.TextField(blank=True, null=True, verbose_name='Offer Description'),
        ),
    ]
