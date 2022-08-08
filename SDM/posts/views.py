from django.shortcuts import render

# Create your views here.


def test(request):
    context = {
        'var': '🤘'
    }
    return render(request, 'test.html', context)


def add_debt(request):
    context = {}
    return render(request, "add_debt.html", context)
