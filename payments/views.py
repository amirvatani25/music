import logging

from django.shortcuts import redirect
from django.urls import reverse

from azbankgateways.exceptions import AZBankGatewaysException

import logging

from django.http import HttpResponse, Http404

from azbankgateways import bankfactories, models as bank_models, default_settings as settings
from django.utils import timezone
from datetime import timedelta


def go_to_gateway_view(request):
    # خواندن مبلغ از هر جایی که مد نظر است
    profile = request.user.profile
    subscription = profile.subscription_set.latest('create')
    amountOfSub = subscription.subscriptions
    if amountOfSub == '50000':
        amount = int(amountOfSub)
    if amountOfSub == '100000':
        amount = int(amountOfSub)
    if amountOfSub == '200000':
        amount = int(amountOfSub)
    if amountOfSub == '500000':
        amount = int(amountOfSub)

    # تنظیم شماره موبایل کاربر از هر جایی که مد نظر است
    user_mobile_number = '+989112221234'  # اختیاری

    factory = bankfactories.BankFactory()
    try:
        bank = factory.auto_create()  # or factory.create(bank_models.BankType.BMI) or set identifier
        bank.set_request(request)
        bank.set_amount(amount)
        # یو آر ال بازگشت به نرم افزار برای ادامه فرآیند
        bank.set_client_callback_url('/callback-gateway/')
        bank.set_mobile_number(user_mobile_number)  # اختیاری

        # در صورت تمایل اتصال این رکورد به رکورد فاکتور یا هر چیزی که بعدا بتوانید ارتباط بین محصول یا خدمات را با این
        # پرداخت برقرار کنید.
        bank_record = bank.ready()

        # هدایت کاربر به درگاه بانک
        return bank.redirect_gateway()
    except AZBankGatewaysException as e:
        logging.critical(e)
        # TODO: redirect to failed page.
        raise e

def callback_gateway_view(request):
    tracking_code = request.GET.get(settings.TRACKING_CODE_QUERY_PARAM, None)
    if not tracking_code:
        logging.debug("این لینک معتبر نیست.")
        raise Http404

    try:
        bank_record = bank_models.Bank.objects.get(tracking_code=tracking_code)
    except bank_models.Bank.DoesNotExist:
        logging.debug("این لینک معتبر نیست.")
        raise Http404

    # در این قسمت باید از طریق داده هایی که در بانک رکورد وجود دارد، رکورد متناظر یا هر اقدام مقتضی دیگر را انجام دهیم
    if bank_record.is_success:
        # پرداخت با موفقیت انجام پذیرفته است و بانک تایید کرده است.
        # می توانید کاربر را به صفحه نتیجه هدایت کنید یا نتیجه را نمایش دهید.
        return redirect('vipSet')

    # پرداخت موفق نبوده است. اگر پول کم شده است ظرف مدت ۴۸ ساعت پول به حساب شما بازخواهد گشت.
    return HttpResponse("پرداخت با شکست مواجه شده است. اگر پول کم شده است ظرف مدت ۴۸ ساعت پول به حساب شما بازخواهد گشت.")


def vipset(request):
    profile = request.user.profile
    subscription = profile.subscription_set.latest('create')
    amountOfSub = subscription.subscriptions
    if amountOfSub == '50000':
        profile.vip = True
        now_date = timezone.now()
        profile.payment_time = timezone.now()
        profile.expire_date = now_date + timedelta(days=30)
        profile.save()
    if amountOfSub == '100000':
        profile.vip = True
        now_date = timezone.now()
        profile.payment_time = timezone.now()
        profile.expire_date = now_date + timedelta(days=90)
        profile.save()
    if amountOfSub == '200000':
        profile.vip = True
        now_date = timezone.now()
        profile.payment_time = timezone.now()
        profile.expire_date = now_date + timedelta(days=180)
        profile.save()
    if amountOfSub == '500000':
        profile.vip = True
        now_date = timezone.now()
        profile.payment_time = timezone.now()
        profile.expire_date = now_date + timedelta(days=365)
        profile.save()

    return redirect('account')