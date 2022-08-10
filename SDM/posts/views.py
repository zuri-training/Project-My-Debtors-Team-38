from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages
from .models import Debt

# Create your views here.


@login_required(login_url='accounts:login')
def add_debt(request): 
    if request.method == 'POST':
        if FILES.get('image') != None:
            full_name = request.POST['full_name']
            student_id = request.POST['student_id']
            image = request.POST.get('image')
            date_of_withdrawal = request.POST['date_of_withdrawal']
            debt_incured = request.POST['debt_incured']
            gender = request.POST['gender']
            class_of_withdrawal = request.POST['class_of_withdrawal']
            interest_incured = request.POST['interest_incured']

            form = {
               'full_name':full_name,
               'student_id': student_id,
               'image': image,
               'date_of_withdrawal': date_of_withdrawal,
               'debt_incured': debt_incured,
               'gender': gender,
               'class_of_withdrawal': class_of_withdrawal,
               'interest_incured': interest_incured
               }

            if form.is_valid():
                new_full_name = form.cleaned_data['full_name']
                new_student_id = form.cleaned_data['student_id']
                new_image = form.cleaned_data['image']
                new_date_of_withdrawal = form.cleaned_data['date_of_withdrawal']
                new_debt_incured = form.cleaned_data['debt_incured']
                new_gender = form.cleaned_data['gender']
                new_class_of_withdrawal = form.cleaned_data['class_of_withdrawal']
                new_interest_incured = form.cleaned_data['interest_incured']
            
                new_debt = Debt(
                    full_name = new_full_name,
                    student_id = new_student_id,
                    image = new_image,
                    date_of_withdrawal = new_date_of_withdrawal,
                    debt_incured = new_debt_incured,
                    gender = new_gender,
                    class_of_withdrawal = new_class_of_withdrawal,
                    interest_incured = new_interest_incured
                )
                new_debt.save()
                return redirect('add_debt')

        else:
            return redirect('add_debt')


    context = {
        'success':True
    }
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
