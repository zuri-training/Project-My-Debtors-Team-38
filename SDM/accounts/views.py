from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import SchoolRegistrationForm, GuardianRegistrationForm
from django.db.models import Q
from django.contrib import messages


def select_reg_page(request):
    context = {}
    return render(request, 'accounts/select_reg.html', context)


def school_register_page(request, *args, **kwargs):
    user = request.user
    if user.is_authenticated:
        print(user.role)

        return HttpResponse("You are already authenticated as " + str(user.email))

    context = {}
    if request.POST:
        form = SchoolRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email').lower()
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            destination = kwargs.get("next")
            if destination:
                return redirect(destination)
            return redirect('')
        else:
            context['registration_form'] = form

    else:
        form = SchoolRegistrationForm()
        context['registration_form'] = form
    return render(request, 'accounts/sch_reg.html', context)


def guardian_register_page(request, *args, **kwargs):
    user = request.user
    if user.is_authenticated:
        return HttpResponse("You are already authenticated as " + str(user.email))

    context = {}
    if request.POST:
        form = GuardianRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email').lower()
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            destination = kwargs.get("next")
            if destination:
                return redirect(destination)
            return redirect('posts/')
        else:
            context['registration_form'] = form

    else:
        form = GuardianRegistrationForm()
        context['registration_form'] = form
    return render(request, 'accounts/gdn_reg.html', context)


def login_page(request):
    context = {}
    return render(request, 'accounts/login.html', context)


def forgot_password(request):
    return render(request, 'accounts/forgot_pswd.html')


@login_required(login_url='login')
def school_dashboard_page(request):
    context = {}
    return render(request, 'accounts/sch_dshbd.html', context)


@login_required(login_url='login')
def guardian_home_page(request):
    context = {}
    return render(request, 'accounts/gdn_wlc.html', context)


@login_required(login_url='login')
def guardian_add_child_page(request):
    context = {}
    return render(request, 'accounts/chd_form.html', context)
