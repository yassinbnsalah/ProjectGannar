# Generated by Django 3.2.8 on 2021-11-30 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_auto_20211127_2006'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='is_requested',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='ouvrier',
            name='nb_ticket',
            field=models.IntegerField(null=True),
        ),
    ]