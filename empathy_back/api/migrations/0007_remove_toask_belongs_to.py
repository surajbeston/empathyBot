# Generated by Django 3.0.7 on 2020-06-27 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_toask_redirection'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='toask',
            name='belongs_to',
        ),
    ]
