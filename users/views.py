from django.shortcuts import render , redirect
import json
import requests
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login , authenticate , logout
from django.contrib import messages
from django.db.models import Q
from .forms import customUserCreationForm,profileForm
from musicbeats.forms import playlistForm
from  django.http import  HttpResponse , HttpResponseRedirect


# Create your views here.



def loginUser(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('account')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']


        captcha_token = request.POST.get("g-recaptcha-response")
        cap_url = "https://www.google.com/recaptcha/api/siteverify"
        captcha_secret = "6LfF6wkeAAAAAFOJdHxRLAOrDL6ptJKJMT0Wjgtm"
        cap_data = {"secret": captcha_secret, "response": captcha_token}
        cap_server_response = requests.post(url=cap_url, data=cap_data)
        cap_json = json.loads(cap_server_response.text)
        if cap_json['success'] == False:
            messages.error(request, 'کپچا را اشتباه وارد کردید!')
            #TODO: error massages
            return HttpResponseRedirect("/users/login/")


        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request , 'username does not exist!')

        user = authenticate(request,username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            messages.error(request, 'username or password is incorrect...')

    return render(request, 'users/login.html')


def logoutUser(request):
    logout(request)
    messages.info(request, 'User was loged out')
    return redirect('login')

def registerUser(request):
    page = 'register'
    form = customUserCreationForm()

    if request.method == 'POST':
        form = customUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'user account was created!')

            login(request,user)
            return redirect('homepage')

        else:
            messages.error(request, 'an error has occurred during registration!')


    context = {'page':page , 'form':form}
    return render(request, 'users/register.html', context)


def userProfile(request , pk):
    profile = Profile.objects.get(id=pk)
    context = {'profile':profile}
    return render(request, 'users/user-profile.html',context)


@login_required(login_url='login')
def userAccount(request):
    profile= request.user.profile
    form = profileForm

    if request.method == 'POST':
        form = playlistForm(request.POST)
        if form.is_valid():
            plalist = form.save(commit=False)
            plalist.owner = profile
            plalist.save()
            return redirect('account')
    form = playlistForm
    context = {'profile':profile,'form':form}
    return render(request,'users/account.html',context)

@login_required(login_url='login')
def editAccount(request):
    profile = request.user.profile
    form = profileForm(instance=profile)
    if request.method == 'POST':
        form = profileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()

            return redirect('account')

    context = {'form': form , 'profile':profile}
    return render(request, 'users/profile_form.html', context)






