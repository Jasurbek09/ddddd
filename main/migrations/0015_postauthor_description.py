# Generated by Django 3.2.5 on 2021-07-23 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='postauthor',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]