# Generated by Django 3.2.5 on 2021-07-24 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_postauthor_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='podpischiki',
            name='email',
            field=models.CharField(max_length=200),
        ),
    ]