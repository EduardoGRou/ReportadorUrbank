# Generated by Django 3.2.4 on 2021-09-07 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0002_auto_20210907_1619'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipoinversion',
            name='toWhom',
            field=models.IntegerField(default=0),
        ),
    ]