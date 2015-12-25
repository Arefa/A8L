# -*-coding: utf-8 -*-
from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from collectinfo.forms import UserForm, UserProfileForm


def index(request):
    return render(request, 'collectinfo/index.html', {})


def signup(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid and profile_form.is_valid:
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registered = True
        else:
            print user_form.errors, profile_form.errors
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request,
                  'collectinfo/signup.html',
                  {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                # return render(request, 'collectinfo/home.html', {})
                return HttpResponseRedirect('/collectinfo/home/')
            else:
                return HttpResponse('该账户未激活!')
        else:
            print "无效登录详情： {0}, {1}".format(username, password)
            return HttpResponse('无效登录详情支持。')
    else:
        return render(request, 'collectinfo/signin.html', {})


@login_required
def signout(request):
    logout(request)
    return HttpResponseRedirect('/collectinfo/')


@login_required
def home(request):
    return render(request, 'collectinfo/home.html', {})
