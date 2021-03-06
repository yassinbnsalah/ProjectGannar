# Generated by Django 3.2.8 on 2021-10-31 02:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20211030_1539'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ouvrier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job', models.CharField(max_length=50, null=True)),
                ('desponibility', models.CharField(max_length=50, null=True)),
                ('description', models.CharField(max_length=250, null=True)),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.client')),
            ],
        ),
    ]
