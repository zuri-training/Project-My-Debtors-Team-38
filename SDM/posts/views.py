from email import message
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages
from .models import Debt, Comments, Contend, Post

# Create your views here.


def test(request):
    context = {
        'var': '🤘'
    }
    return render(request, 'test.html', context)


#@login_required(login_url='accounts:login')
def add_debt(request):
    page = 'add_debt'
    context = {}

    if request.method == "POST":
        #ensures an image is uploaded along with the form 
        if request.FILES.get('image') != None: 
            image = request.POST.get("image")
            full_name = request.POST['full_name']
            student = request.POST['student_id']
            date_of_withdr = request.POST['date_of_withdr']
            debt_incured = request.POST['debt_incured']
            gender = request.POST['gender']
            class_of_withdr = request.POST['class_of_withdr']
            interest_incured = request.POST['interest_incured']
            # Instance for debt of student
            student_debt = Debt.objects.create(
                image=image, full_name=full_name, student=student,
                date_of_withdrawal=date_of_withdr, debt_incured=debt_incured,
                gender=gender,class_of_withdrawal=class_of_withdr,interest_incured=interest_incured
            )
            student_debt.save()
   
        else:
            messages.error(request, "Please upload picture of student!")
            return redirect("posts:add_debt")


    return render(request, "posts/add_debt.html", context)


@login_required(login_url='accounts:login')
def debt_confirm(request):
    context = {}
    return render(request, "posts/debt_confirm.html", context)


@login_required(login_url='accounts:login')
def debt_sus(request):
    context = {}
    return render(request, "posts/debt_sus.html", context)


@login_required(login_url='accounts:login')
def contend_sus(request):
    context = {}
    return render(request, "posts/contend_sus.html", context)


@login_required(login_url='accounts:login')
def gdn_clear(request):
    context = {}
    return render(request, "posts/gdn_clear.html", context)


@login_required(login_url='accounts:login')
def gdn_confirm(request):
    context = {}
    return render(request, "posts/gdn_confirm.html", context)


@login_required(login_url='accounts:login')
def gdn_contend(request):
    context = {}
    return render(request, "posts/gdn_contend.html", context)


@login_required(login_url='accounts:login')
def sch_dir(request):
    context = {}
    return render(request, "posts/sch_dir.html", context)


@login_required(login_url='accounts:login')
def sch_backlog(request):
    context = {}
    return render(request, "posts/sch_backlog.html", context)


@login_required(login_url='accounts:login')
def sch_contend(request):
    context = {}
    return render(request, "posts/sch_contend.html", context)


@login_required(login_url='accounts:login')
def sch_post(request):
    context = {}
    return render(request, "posts/sch_post.html", context)


@login_required(login_url='accounts:login')
def sch_review(request):
    context = {}
    return render(request, "posts/sch_review.html", context)

@login_required(login_url='accounts:login')
def guardian_add_child_page(request):
    context = {}
    return render(request, "posts/chd_form.html", context)