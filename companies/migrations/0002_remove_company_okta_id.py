# Generated by Django 3.0.5 on 2020-04-26 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='okta_id',
        ),
    ]