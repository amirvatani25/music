from django.contrib import admin
from .models import Profile , Payment , Subscription
# Register your models here.


admin.site.register(Profile)
admin.site.register(Payment)
admin.site.register(Subscription)