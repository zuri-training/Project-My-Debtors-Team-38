from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from posts.models import Debt,Student,School
# Create your views here.


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








def contend_sus(request):
    context = {}
    return render(request,'posts/contend_sus.html', context)
