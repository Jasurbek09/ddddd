# Generated by Django 3.2.5 on 2021-07-24 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_auto_20210724_1616'),
    ]

    operations = [
        migrations.AddField(
            model_name='others',
            name='my_qualifications',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='others',
            name='my_qualifications_desc',
            field=models.TextField(blank=True),
        ),
    ]
