# Generated by Django 3.2.5 on 2021-07-24 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_auto_20210724_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='others',
            name='my_offered_services_desc',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='others',
            name='my_offered_services_title',
            field=models.TextField(),
        ),
    ]
