# Generated by Django 2.0 on 2017-12-28 20:02

from django.db import migrations, models
import tweets.models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0007_tweet_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='text',
            field=models.CharField(max_length=120, validators=[tweets.models.validate_text]),
        ),
    ]
