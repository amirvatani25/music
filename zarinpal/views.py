from django.http import HttpResponse
from django.shortcuts import redirect
import requests
import json
from zeep import Client

MERCHANT = 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX'
client = Client('https://www.zarinpal.com/pg/services/webGate/wsdl')

description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
mobile = '09123456789'  # Optional
# Important: need to edit for realy server.
CallbackURL = 'http://localhost:8000/zarinpal/verify/'


def send_request(request,price):
    global amount
    amount = price
    result = client.service.PaymentRequest(MERCHANT,amount,description,request.user.email,mobile,CallbackURL)
    if result.Status == 100:
        return redirect('https://www.zarinpal.com/pg/startPay/' + str(result.Authority))
    else:
        return HttpResponse('Error code: ' + str(result.Status))



def verify(request):
    if request.GET.get('Status') == 'OK':
        result = client.service.PaymentVerificatin(MERCHANT,request.GET['Authority'],amount)
        if result.Status == 100:
            return HttpResponse('Transaction success.\nRefID: ' + str(result.RefID))
        elif result.Status == 101:
            return HttpResponse('Transaction submitted : ' + str(result.Status))
        else:
            return HttpResponse('Transaction failed.\nStatus: ' + str(result.Status))
    else:
        return HttpResponse('Transaction failed or canceled by user')