# Generated by Django 3.2 on 2023-03-03 21:17

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='uuid',
            field=models.UUIDField(blank=True, default=uuid.uuid4, null=True),
        ),
    ]