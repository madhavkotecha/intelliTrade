# Generated by Django 4.2.4 on 2023-08-16 07:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_watchlist_delete_scripmaster'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlist',
            name='token',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]