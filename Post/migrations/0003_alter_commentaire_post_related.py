# Generated by Django 3.2.8 on 2021-12-04 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0002_commentaire'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentaire',
            name='Post_related',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Post.post'),
        ),
    ]