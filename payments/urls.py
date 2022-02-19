from django.urls import path
from . import views

urlpatterns = [
    path('u-sent-ur-url-and-now-i-want-to-change-your-vip-pos/',views.vipset,name='vipSet')


]