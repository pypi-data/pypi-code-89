# Generated by Django 3.1.4 on 2021-05-17 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_auto_20210505_2037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='sampling',
            field=models.CharField(choices=[('Sequential sampling', 'Tasks are ordered by Data manager ordering'), ('Uniform sampling', 'Tasks are chosen randomly'), ('Uncertainty sampling', 'Tasks are chosen according to model uncertainty scores (active learning mode)')], default='Sequential sampling', max_length=100, null=True),
        ),
    ]
