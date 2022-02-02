# Generated by Django 3.2.11 on 2022-02-02 07:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('musicbeats', '0025_alter_adminplaylist_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='playlist',
            old_name='songs',
            new_name='song',
        ),
        migrations.AlterField(
            model_name='playlist',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
