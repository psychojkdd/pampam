# Generated by Django 5.1.3 on 2024-11-14 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_post2'),
    ]

    operations = [
        migrations.AddField(
            model_name='contentblock',
            name='short_description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]