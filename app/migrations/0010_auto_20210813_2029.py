# Generated by Django 3.2.6 on 2021-08-13 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20210813_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='facebook_link',
            field=models.CharField(default='https://facebook.com/<django.db.models.fields.CharField>', max_length=300),
        ),
        migrations.AlterField(
            model_name='customer',
            name='github_link',
            field=models.CharField(default='https://github.com/<django.db.models.fields.CharField>', max_length=300),
        ),
        migrations.AlterField(
            model_name='customer',
            name='instagram_link',
            field=models.CharField(default='https://instagram.com/<django.db.models.fields.CharField>', max_length=300),
        ),
        migrations.AlterField(
            model_name='customer',
            name='twitter_link',
            field=models.CharField(default='https://twitter.com/<django.db.models.fields.CharField>', max_length=300),
        ),
    ]