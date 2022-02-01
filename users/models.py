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
    create = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,primary_key=True,unique=True,
                          editable=False)
    # paid_until = models.DateField(null=True,blank=True)
    # stripeCustomerId = models.CharField(max_length=255)
    # stripeSubscriptionId = models.CharField(max_length=255)


    # def set_paid_until(self,date_or_timestamp):
    #     if isinstance(date_or_timestamp,int):
    #         paid_until = date.fromtimestamp(date_or_timestamp)
    #     elif isinstance(date_or_timestamp,str):
    #         paid_until = date.fromtimestamp(int(date_or_timestamp))
    #     else:
    #         paid_until = date_or_timestamp
    #
    #     self.paid_until = paid_until
    #     self.save()
    #
    # def has_paid(
    #         self
    #         ,current_date = datetime.date.today()
    # ):
    #     if self.paid_until is None:
    #         return False
    #
    #     return  current_date < self.paid_until

    def __str__(self):
        return str(self.username)


