# Generated by Django 3.2.8 on 2021-11-18 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_client_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='image',
        ),
    ]
