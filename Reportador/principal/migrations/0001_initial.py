# Generated by Django 3.2.4 on 2021-09-03 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UrbUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('username', models.CharField(max_length=20, unique=True, verbose_name='User name')),
                ('uid', models.AutoField(primary_key=True, serialize=False, verbose_name='User ID')),
                ('firstname', models.CharField(max_length=50, verbose_name='First name')),
                ('lastname', models.CharField(max_length=20, verbose_name='Last name')),
                ('phone', models.CharField(max_length=20, unique=True, verbose_name='Phone number')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='Email address')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last Login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('monto_inver', models.CharField(max_length=150)),
                ('taze_interes', models.EmailField(max_length=200)),
                ('fecha_termino', models.DateField()),
                ('pagos', models.IntegerField()),
                ('donde_inver', models.CharField(max_length=200)),
                ('place', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='principal.urbuser')),
            ],
        ),
        migrations.CreateModel(
            name='TipoInversion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('donde', models.CharField(max_length=100)),
                ('dollars', models.IntegerField()),
                ('euros', models.IntegerField()),
                ('shivas', models.IntegerField()),
                ('ethers', models.IntegerField()),
                ('bitcoins', models.IntegerField()),
                ('cardanos', models.IntegerField()),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Inversion_User', to='principal.user')),
            ],
        ),
        migrations.CreateModel(
            name='Pagos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('paymentName', models.CharField(max_length=100)),
                ('fecha_pago', models.DateField()),
                ('concepto', models.CharField(max_length=100)),
                ('monto', models.IntegerField()),
                ('user_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Payment_User', to='principal.user')),
            ],
        ),
    ]