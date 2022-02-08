# Generated by Django 3.2.5 on 2021-07-17 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20210715_2013'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='coment_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='comment',
            name='email',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='comment',
            name='author_logo',
            field=models.ImageField(blank=True, default='', upload_to='upload'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='pub_date',
            field=models.DateField(blank=True),
        ),
    ]