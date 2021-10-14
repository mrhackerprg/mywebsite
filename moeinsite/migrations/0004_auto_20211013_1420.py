# Generated by Django 3.2.4 on 2021-10-13 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moeinsite', '0003_alter_info_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='info',
            name='facebook',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='info',
            name='instagrm',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='info',
            name='phonenumber',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AddField(
            model_name='info',
            name='twitter',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='info',
            name='youtube',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]