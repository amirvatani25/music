# Generated by Django 3.2.11 on 2022-01-31 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicbeats', '0024_auto_20220129_0110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminplaylist',
            name='image',
            field=models.ImageField(blank=True, default='profiles/user-defualt.png', null=True, upload_to='adminplaylists/'),
        ),
    ]
