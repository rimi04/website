# Generated by Django 2.2 on 2019-11-08 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thereg', '0013_auto_20191026_2246'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='varified',
            field=models.BooleanField(default=False),
        ),
    ]
