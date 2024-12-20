# Generated by Django 5.1.4 on 2024-12-20 02:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('ticket_id', models.AutoField(primary_key=True, serialize=False)),
                ('event_name', models.CharField(max_length=255)),
                ('event_time', models.DateTimeField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.event')),
            ],
        ),
    ]