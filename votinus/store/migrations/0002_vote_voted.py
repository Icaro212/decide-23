# Generated by Django 2.0 on 2018-02-24 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote',
            name='voted',
            field=models.DateTimeField(auto_now=True),
        ),
    ]