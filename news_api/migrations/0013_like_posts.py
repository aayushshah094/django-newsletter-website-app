# Generated by Django 3.2.7 on 2021-11-18 06:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news_api', '0012_auto_20211118_0104'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='posts',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='news_api.post'),
        ),
    ]