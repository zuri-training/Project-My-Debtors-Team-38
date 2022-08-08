from django.shortcuts import render

# Create your views here.

def landing_page(request):
    return render(request, 'base/landing.html')

def school_reg_page(request):
    return render(request, 'base/school_reg_with_us.html')

def contact_us_page(request):
    return render(request, 'base/contact_us.html')
