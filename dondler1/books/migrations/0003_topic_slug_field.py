# Generated by Django 2.2.1 on 2019-05-24 16:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_remove_topic_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='slug_field',
            field=models.SlugField(default=datetime.datetime(2019, 5, 24, 16, 49, 27, 691185, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
