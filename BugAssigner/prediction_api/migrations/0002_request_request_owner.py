# Generated by Django 3.1.7 on 2022-01-08 14:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('prediction_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='request_owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='request_owner', to='auth.user'),
            preserve_default=False,
        ),
    ]
