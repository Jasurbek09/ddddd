# Generated by Django 3.2.5 on 2021-07-15 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_faq_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(blank=True, upload_to='upload')),
                ('title', models.CharField(default='title', max_length=200)),
                ('description', models.TextField()),
            ],
        ),
    ]