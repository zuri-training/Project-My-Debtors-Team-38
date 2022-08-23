from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import SchoolRegistrationForm, GuardianRegistrationForm
from django.db.models import Q
from django.contrib import messages
from .models import Guardian, School, GuardianProfile, SchoolProfile, GuardianChild, Student
from django.contrib.auth import get_user_model


User = get_user_model()


def select_reg_page(request):
    nav = 'nav'
    page = 'school_reg'

    if request.user.is_authenticated:
        if request.user.role == 'GUARDIAN':
            return redirect('acounts:gdn_wlc')
        elif request.user.role == 'SCHOOL':
            return redirect('accounts:sch_dshbd')

    context = {'page': page,
               'nav': nav}
    return render(request, 'accounts/select_reg.html', context)


def school_register_page(request, *args, **kwargs):
    nav = 'nav'
    page = 'school_reg'

    if request.user.is_authenticated:
        if request.user.role == 'GUARDIAN':
            return redirect('acounts:gdn_wlc')
        elif request.user.role == 'SCHOOL':
            return redirect('accounts:sch_dshbd')

    if request.method == 'POST':
        password = request.POST.get('password1')
        print(password)
        password = make_password(password)

        school = School.objects.create(
            email=request.POST.get('email').lower(),
            name=request.POST.get('name').title(),
            password=password
        )
        school.save()
        login(request, school,
              backend='django.contrib.auth.backends.AllowAllUsersModelBackend')
        return redirect('posts:sch_dir')
    else:
        messages.error(request, 'An error occured during registration')

    context = {
        'nav': nav,
        'page': page,
    }

    return render(request, 'accounts/sch_reg.html', context=context)


def guardian_register_page(request, *args, **kwargs):
    nav = 'nav'
    page = 'gdn_reg'

    if request.user.is_authenticated:
        if request.user.role == 'GUARDIAN':
            return redirect('acounts:gdn_wlc')
        elif request.user.role == 'SCHOOL':
            return redirect('accounts:sch_dshbd')

    if request.method == 'POST':
        password = request.POST.get('password1')
        password = make_password(password)

        try:
            guardian = Guardian.objects.create(
                email=request.POST.get('email').lower(),
                name=request.POST.get('name').title(),
                password=password
            )
        except:
            messages.error(request, 'User already exists')
        else:
            guardian.save()
            login(request, guardian,
                  backend='django.contrib.auth.backends.AllowAllUsersModelBackend')
            return redirect('accounts:gdn_wlc')
    else:
        messages.error(request, 'An error occured during registration')

    context = {
        'nav': nav,
        'page': page,
    }

    return render(request, 'accounts/gdn_reg.html', context=context)


def login_page(request):
    nav = 'nav'
    page = 'login'

    if request.user.is_authenticated:
        if request.user.role == 'GUARDIAN':
            return redirect('accounts:gdn_wlc')
        elif request.user.role == 'SCHOOL':
            return redirect('posts:sch_dir')

    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, 'User does not exist')
        else:
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(
                    request, user, backend='django.contrib.auth.backends.AllowAllUsersModelBackend')

                if request.user.role == 'GUARDIAN':
                    return redirect('accounts:gdn_wlc')
                elif request.user.role == 'SCHOOL':
                    return redirect('posts:sch_dir')

            else:
                messages.error(request, 'Username or Password does not exist')

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
def school_profile(request, pk):
    nav = 'nav'
    page = 'sch_profile'

    if request.user.role == 'SCHOOL':
        school = School.objects.get(id=pk)
        context = {'nav': nav,
                   'page': page}
        return render(request, 'accounts/sch_profile.html', context=context)

    else:
        return HttpResponse('you are not allowed here!!')


@login_required(login_url='accounts:login')
def guardian_home_page(request):
    context = {}

    if request.user.role == 'GUARDIAN':
        guardian = request.user
        # print(guardian.name)
        try:
            children = GuardianChild.objects.all()
            students = Student.objects.all()
            # print(children)
        except:
            pass
        else:
            context['children'] = children
            context['students'] = students

        return render(request, 'accounts/gdn_wlc.html', context=context)
    else:
        return HttpResponse('you are not allowed here!!')
