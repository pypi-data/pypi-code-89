# Generated by Django 3.1.7 on 2021-03-16 17:07

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0009_test_drop_table_with_foreign_key_reference_part2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('name', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('name', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('toppings', models.ManyToManyField(to='testapp.Topping')),
            ],
        ),
    ]
