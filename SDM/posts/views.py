from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages
from .models import Post, Contend, Comments
from accounts.models import Student


#@login_required(login_url='accounts:login')
def add_debt(request):
    page = 'add_debt'
    context = {}
    if request.method == 'POST':
        if request.FILES.get('avatar') != None: 
            school = request.user
            student = Student.objects.create(
                school=school,
                student_id=request.POST.get('std-id'),
                name=request.POST.get('fname'),
                gender=request.POST.get('gender'),
                class_of_withdrawal=request.POST.get('cl-wtd'),
                date_of_withdrawal=request.POST.get('dt-wtd'),
                debt_incured=request.POST.get('debt-in'),
                interest_incured=request.POST.get('inter-in'),
                age=request.POST.get('age'),
                avatar=request.POST.get('avatar')
            )
            student.save()
            Post.objects.create(school=student.school, student=student)
            return redirect('posts:sch_dir')
        else:
            messages.error(request, "Please upload picture of student!")
            return redirect("posts:add_debt")
    else:
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


# @login_required(login_url='login')
def guardian_add_child_page(request):
    page = 'chd_form'
    user = request.user
    if request.method == 'POST':
        guardian = user
        student_id = request.POST.get('student_id')
        name = request.POST.get('name')
        school = request.POST.get('school')
        gender = request.POST.get('gender')
        relationship = request.POST.get('relationship')

        try:
            child = GuardianChild.objects.create(guardian=guardian, student_id=student_id,
                                                 name=name, school_name=school, gender=gender, 
                                                 relationship=relationship)
            # print(child.name)

        except:
            pass
        else:
            return redirect('accounts:gdn_wlc')

    context = {
        'page': page,
    }
    return render(request, 'posts/chd_form.html', context)


# @login_required(login_url='accounts:login')
def gdn_contend(request):
    page = "gdn_contend"
    context = {}

    guardian = request.user

    if request.method == "POST":
        reason = request.POST.get("reason")
        receipt = request.POST.get("receipt")
    
        contend = Contend(guardian=guardian, reason=reason, receipt=receipt,)
        contend.save()

    else:
        return redirect("posts:gdn_contend")

    return render(request, "posts/gdn_contend.html", context)




# @login_required(login_url='accounts:login')
def sch_dir(request):
    page = 'sch_dir'

    if request.user.role != "SCHOOL":
        return redirect('base:home')
    students = Student.objects.all()
    posts = Post.objects.filter(school=request.user)
    for post in posts:
        print(post.student.name)

    context = {
        'students': students,
        'posts': posts,
    }
    return render(request, "posts/sch_dir.html", context)




@login_required(login_url='accounts:login')
def sch_backlog(request):
    context = {}
    return render(request, "posts/sch_backlog.html", context)




#@login_required(login_url='accounts:login')
def sch_contend(request):
    student = Student.objects.all()
    posts = Post.objects.all(),
    contends = Contend.objects.all()

    context = {
        "student":student,
        "posts":posts,
        "contends":contends,
    }
    return render(request, "posts/sch_contend.html", context)



# @login_required(login_url='accounts:login')
def sch_comment(request, pk):
    if request.user.role != "SCHOOL":
        return redirect('base:home')

    post = Post.objects.get(id=pk)
    post_comments = post.comments_set.all()

    if request.method == 'POST':
        comments = Comments.objects.create(
            school=request.user, post=post, body=request.POST.get('body'))
        return redirect('posts:sch_comment', pk=post.id)

    context = {
        'post': post,
        'post_comments': post_comments,
    }
    return render(request, "posts/posts.html", context)


# @login_required(login_url='accounts:login')
def sch_post(request):
    if request.user.role != "SCHOOL":
        return redirect('base:home')

    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, "posts/post_comment.html", context)




# @ login_required(login_url='accounts:login')
def sch_review(request):
    context = {}
    return render(request, "posts/sch_review.html", context)



@login_required(login_url='accounts:login')
def guardian_add_child_page(request):
    context = {}
    return render(request, "posts/chd_form.html", context)