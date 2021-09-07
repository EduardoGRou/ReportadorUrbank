# Generated by Django 3.2.4 on 2021-09-07 16:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pagos',
            name='user_name',
        ),
        migrations.RemoveField(
            model_name='tipoinversion',
            name='user',
        ),
        migrations.RemoveField(
            model_name='user',
            name='place',
        ),
        migrations.AddField(
            model_name='pagos',
            name='toWhom',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='pagos',
            name='fecha_pago',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='pagos',
            name='monto',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='tipoinversion',
            name='bitcoins',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='tipoinversion',
            name='cardanos',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='tipoinversion',
            name='dollars',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='tipoinversion',
            name='ethers',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='tipoinversion',
            name='euros',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='tipoinversion',
            name='shivas',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='fecha_termino',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='user',
            name='pagos',
            field=models.IntegerField(default=0),
        ),
    ]
