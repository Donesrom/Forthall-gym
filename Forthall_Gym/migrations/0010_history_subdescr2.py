# Generated by Django 4.0.3 on 2022-04-10 14:34

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('Forthall_Gym', '0009_rename_subtitle_history_subtitle1_history_subtitle2'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='Subdescr2',
            field=tinymce.models.HTMLField(null=True),
        ),
    ]
