from django.shortcuts import render

# Create your views here.


def landing_page(request):
    nav = 'nav'
    page = 'home'
    context = {'page': page,
               'nav': nav, }
    return render(request, 'base/index.html', context=context)


def school_list_page(request):
    nav = 'nav'
    page = 'sch_list'
    context = {'page': page,
               'nav': nav, }
    return render(request, 'base/sch_list.html', context=context)


def contact_us_page(request):
    nav = 'nav'
    page = 'contact_us'
    context = {'page': page,
               'nav': nav, }
    return render(request, 'base/contact.html', context=context)
