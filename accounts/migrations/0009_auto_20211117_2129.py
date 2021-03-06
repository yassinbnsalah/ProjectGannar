# Generated by Django 3.2.8 on 2021-11-17 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20211104_1609'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('nb_employees', models.IntegerField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='ouvrier',
            name='categorie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.categorie'),
        ),
    ]
