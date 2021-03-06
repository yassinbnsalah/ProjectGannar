# Generated by Django 3.2.8 on 2021-12-08 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_auto_20211130_2225'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=250, null=True)),
                ('date_repport', models.DateField(auto_now_add=True)),
                ('fromcl', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.client')),
                ('tocl', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.ouvrier')),
            ],
        ),
    ]
