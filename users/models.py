import datetime
from datetime import date
from django.db import models
from django.contrib.auth.models import User
import uuid
from django.db.models.signals import post_save , post_delete

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True, blank=True)
    name = models.CharField(max_length=200, blank=True,null=True)
    familyName = models.CharField(max_length=200, blank=True,null=True)
    username = models.CharField(max_length=200, blank=True , null=True)
    email = models.EmailField(max_length=500,blank=True,null=True)
    profile_image = models.ImageField(null=True,blank=True,upload_to='profile/',default="profiles/user-defualt.png")
    vip = models.BooleanField(default=False)
    payment_time = models.DateTimeField()
    create = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,primary_key=True,unique=True,
                          editable=False)



    def __str__(self):
        return str(self.username)

    def get_balance_display(self):
        return " {} تومان".format(self.balance)

    def deposit(self, amount):
        self.balance += amount
        self.save()

    def spend(self, amount):
        if self.balance < amount:
            return False
        self.balance -= amount
        self.save()
        return True



class Payment(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="کاربر")
    transaction_time = models.DateTimeField("زمان تراکنش", auto_now_add=True)
    verify = models.BooleanField("نتیجه تراکنش", default=False)

    # transaction_code = models.CharField("رسید تراکنش", max_length=30)

    class Meta:
        verbose_name = "پرداخت ها"
        verbose_name_plural = "پرداخت ها"

