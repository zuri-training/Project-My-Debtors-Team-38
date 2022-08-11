from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import SchoolRegistrationForm, GuardianRegistrationForm
from django.db.models import Q
from django.contrib import messages
from .models import Guardian, School, GuardianProfile, SchoolProfile


def select_reg_page(request):
    nav = 'nav'
    page = 'school_reg'
    context = {'page': page,
               'nav': nav}
    return render(request, 'accounts/select_reg.html', context)


def school_register_page(request, *args, **kwargs):
    nav = 'nav'
    page = 'school_reg'
    context = {}

    if request.method == 'POST':
        password = request.POST.get('password1')
        password = make_password(password)

        school = School.objects.create(
            email=request.POST.get('email').lower(),
            name=request.POST.get('name').title(),
            password=password
        )
        school.save()
        login(request, school,
              backend='django.contrib.auth.backends.AllowAllUsersModelBackend')
        return redirect('accounts:sch_dshbd')
    else:
        messages.error(request, 'An error occured during registration')

    return render(request, 'accounts/sch_reg.html', context)


def guardian_register_page(request, *args, **kwargs):
    nav = 'nav'
    page = 'gdn_reg'
    context = {}

    if request.method == 'POST':
        password = request.POST.get('password1')
        password = make_password(password)

        guardian = Guardian.objects.create(
            email=request.POST.get('email').lower(),
            name=request.POST.get('name').title(),
            password=password
        )
        guardian.save()
        login(request, guardian,
              backend='django.contrib.auth.backends.AllowAllUsersModelBackend')
        return redirect('accounts:gdn_wlc')
    else:
        messages.error(request, 'An error occured during registration')

    return render(request, 'accounts/gdn_reg.html', context=context)


def login_page(request):
    nav = 'nav'
    page = 'login'
    context = {'page': page,
               'nav': nav}
    return render(request, 'accounts/login.html', context=context)


def logout_user(request):
    logout(request)
    return redirect('base:home')


def forgot_password(request):
    nav = 'nav'
    page = 'forgot_password'
    context = {'nav': nav}
    return render(request, 'accounts/forgot_pswd.html', context=context)


@login_required(login_url='accounts:login')
def school_dashboard_page(request):
    if request.user.role == 'SCHOOL':
        context = {}
        return render(request, 'accounts/sch_dshbd.html', context=context)
    else:
        return HttpResponse('you are not allowed here!!')


@login_required(login_url='accounts:login')
def guardian_home_page(request):
    if request.user.role == 'GUARDIAN':
        context = {}
        return render(request, 'accounts/gdn_wlc.html', context=context)
    else:
        return HttpResponse('you are not allowed here!!')
