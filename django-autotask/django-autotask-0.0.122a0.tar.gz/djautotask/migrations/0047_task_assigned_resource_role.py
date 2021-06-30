# Generated by Django 2.1.14 on 2020-02-20 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djautotask', '0046_ticket_assigned_resource_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='assigned_resource_role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='djautotask.Role'),
        ),
    ]
