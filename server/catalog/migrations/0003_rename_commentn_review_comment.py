# Generated by Django 3.2.6 on 2021-08-25 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20210825_1704'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='commentn',
            new_name='comment',
        ),
    ]
