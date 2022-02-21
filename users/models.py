import datetime
from datetime import date
from django.db import models
from django.contrib.auth.models import User
import uuid
from django.db.models.signals import post_save , post_delete

# Create your models here.
from django.utils import timezone


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True, blank=True)
    name = models.CharField(max_length=200, blank=True,null=True)
    familyName = models.CharField(max_length=200, blank=True,null=True)
    username = models.CharField(max_length=200, blank=True , null=True)
    email = models.EmailField(max_length=500,blank=True,null=True)
    profile_image = models.ImageField(null=True,blank=True,upload_to='profile/',default="profiles/user-defualt.png")
    vip = models.BooleanField(default=False)
    payment_time = models.DateTimeField(default=timezone.now(),blank=True, null=True)
    expire_date = models.DateTimeField(default=timezone.now(),blank=True, null=True)
    create = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,primary_key=True,unique=True,
                          editable=False)



    def __str__(self):
        return str(self.username)



class Payment(models.Model):

    user = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="کاربر")
    transaction_time = models.DateTimeField("زمان تراکنش", auto_now_add=True)
    verify = models.BooleanField("نتیجه تراکنش", default=False)

    # transaction_code = models.CharField("رسید تراکنش", max_length=30)

    class Meta:
        verbose_name = "پرداخت ها"
        verbose_name_plural = "پرداخت ها"





class Subscription(models.Model):
    oneMonth = '50000'
    threeMonth = '100000'
    sixMonth = '200000'
    twelveMonth = '500000'
    condition_choices = [
        (oneMonth, 'یک ماهه'),
        (threeMonth, 'سه ماهه'),
        (sixMonth, 'شش ماهه'),
        (twelveMonth, 'یک ساله'),
    ]

    BUY_CONDITION = [
        (oneMonth, 'یک ماهه'),
        (threeMonth, 'سه ماهه'),
        (sixMonth, 'شش ماهه'),
        (twelveMonth, 'یک ساله'),
    ]

    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="کاربر")
    subscriptions = models.CharField(('buy'),max_length=100, choices=BUY_CONDITION, default=oneMonth)
    create = models.DateTimeField(auto_now_add=True)

