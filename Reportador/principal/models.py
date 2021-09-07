from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import datetime

today = datetime.datetime.now()


# Create your models here.

class UrbUserManager(BaseUserManager):

    def create_user(self, email, username, firstname, lastname, phone, password=None):
        if not email:
            raise ValueError("Email entry is required!!")
        if not username:
            raise ValueError("User entry name is required!!")
        if not firstname:
            raise ValueError("First entry name is required!!")
        if not lastname:
            raise ValueError("Last entry name is required!!")
        if not phone:
            raise ValueError("Phone number entry is required!!")

        user = self.model(
            email = self.normalize_email(email),
            username = username,
            firstname = firstname,
            lastname = lastname,
            phone = phone, 
        )
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self, email, username, firstname, lastname, phone, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            firstname = firstname,
            lastname = lastname,
            phone = phone, 
            password = password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using = self._db)
        return user

class UrbUser(AbstractBaseUser):
    username = models.CharField(verbose_name="User name", max_length=20, unique=True)
    uid = models.AutoField(verbose_name="User ID", primary_key=True) 
    firstname = models.CharField(verbose_name="First name", max_length=50)
    lastname = models.CharField(verbose_name="Last name", max_length=20)
    phone = models.CharField(verbose_name="Phone number", max_length=20, unique=True)
    email = models.EmailField(verbose_name="Email address", max_length=60, unique=True) 

    last_login = models.DateTimeField(verbose_name="last Login", auto_now=True)

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username','phone','firstname','lastname']

    objects = UrbUserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField( max_length=100)
    monto_inver=models.CharField(max_length=150)
    taze_interes= models.EmailField(max_length=200)
    fecha_termino=models.DateField(default=datetime.date.today)
    pagos=models.IntegerField(default=0)
    donde_inver=models.CharField(max_length=200)
    


    def __str__(self):
        return self.name

class Pagos(models.Model):
    id = models.AutoField(primary_key=True)
    paymentName=models.CharField(max_length=100)
    fecha_pago=models.DateField(default=datetime.date.today)
    concepto=models.CharField(max_length=100)
    monto=models.IntegerField(default=0)
    toWhom=models.IntegerField(default=0)


class TipoInversion(models.Model):
    id = models.AutoField(primary_key=True)
    donde=models.CharField(max_length=100)
    dollars=models.IntegerField(default=0)
    euros=models.IntegerField(default=0)
    shivas=models.IntegerField(default=0)
    ethers=models.IntegerField(default=0)
    bitcoins=models.IntegerField(default=0)
    cardanos=models.IntegerField(default=0)
    toWhom=models.IntegerField(default=0)
