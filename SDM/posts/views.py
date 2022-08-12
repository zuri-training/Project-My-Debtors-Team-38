from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages
from accounts.models import Student, School

# Create your views here.


def test(request):
    context = {
        'var': '🤘'
    }
    return render(request, 'test.html', context)


# @login_required(login_url='accounts:login')
def add_debt(request):
    context = {}

    if request.method == 'POST':

        student = Student.objects.create(
            student_id = request.POST.get('std-id'),
            name = request.POST.get('fname'),
            gender = request.POST.get('gender'),
            class_of_withdrawal = request.POST.get('cl-wtd'),
            date_of_withdrawal = request.POST.get('dt-wtd'),
            debt_incured = request.POST.get('debt-in'),
            interest_incured = request.POST.get('inter-in'),
            avatar = request.POST.get('formFile'),
        )
        student.save()
    else:
        return render(request, "posts/add_debt.html", context)


# @login_required(login_url='accounts:login')
def debt_confirm(request):
    context = {}
    return render(request, "posts/debt_confirm.html", context)


# @login_required(login_url='accounts:login')
def debt_sus(request):
    context = {}
    return render(request, "posts/debt_sus.html", context)


# @login_required(login_url='accounts:login')
def contend_sus(request):
    context = {}
    return render(request, "posts/contend_sus.html", context)


# @login_required(login_url='accounts:login')
def gdn_clear(request):
    context = {}
    return render(request, "posts/gdn_clear.html", context)


# @login_required(login_url='accounts:login')
def gdn_confirm(request):
    context = {}
    return render(request, "posts/gdn_confirm.html", context)

# @login_required(login_url='login')


def guardian_add_child_page(request):
    context = {}
    return render(request, 'accounts/chd_form.html', context)

# @login_required(login_url='accounts:login')


def gdn_contend(request):
    context = {}
    return render(request, "posts/gdn_contend.html", context)


# @login_required(login_url='accounts:login')
def sch_dir(request):
    context = {}
    return render(request, "posts/sch_dir.html", context)


# @login_required(login_url='accounts:login')
def sch_backlog(request):
    context = {}
    return render(request, "posts/sch_backlog.html", context)


# @login_required(login_url='accounts:login')
def sch_contend(request):
    context = {}
    return render(request, "posts/sch_contend.html", context)


# @login_required(login_url='accounts:login')
def sch_post(request):
    context = {}
    return render(request, "posts/sch_post.html", context)


# @login_required(login_url='accounts:login')
def sch_review(request):
    context = {}
    return render(request, "posts/sch_review.html", context)
