from django.shortcuts import render

# Create your views here.


def landing_page(request):
    return render(request, 'base/index.html')


def school_list_page(request):
    return render(request, 'base/sch_list.html')


def contact_us_page(request):
    return render(request, 'base/contact_us.html')


