# Generated by Django 5.1.4 on 2025-01-05 00:41

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('eventdate', models.DateField()),
                ('cost', models.IntegerField()),
                ('image', models.FileField(blank=True, upload_to='')),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('purchaseDate', models.DateField(auto_now_add=True)),
                ('email', models.EmailField(max_length=254)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.events')),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('cost', models.IntegerField()),
                ('event', models.TextField()),
                ('verified', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=200)),
                ('payment_intent_id', models.CharField(max_length=400)),
                ('last_name', models.CharField(max_length=200)),
                ('sent', models.BooleanField(default=False)),
                ('numTickets', models.IntegerField()),
                ('tickets', models.ManyToManyField(blank=True, to='pages.ticket')),
            ],
        ),
    ]
