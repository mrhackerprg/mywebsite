# Generated by Django 3.2.4 on 2021-10-13 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moeinsite', '0002_alter_info_artist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='title',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
