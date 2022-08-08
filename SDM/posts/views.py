from django.shortcuts import render

# Create your views here.


def test(request):
    context = {
        'var': '🤘'
    }
    return render(request, 'test.html', context)

def sch_list(request):
    context = {}
    return render(request, "sch_list.html", context)

def add_debt(request):
    context = {}
    return render(request,'add_debt.html', context)

def contend_sus(request):
    context = {}
    return render(request,'content_sus.html', context)
