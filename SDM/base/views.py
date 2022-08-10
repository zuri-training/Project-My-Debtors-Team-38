from django.shortcuts import render

# Create your views here.


def landing_page(request):
    page = 'home'
    context = {'page': page}
    return render(request, 'base/index.html', context=context)


def school_list_page(request):
    page = 'sch_list'
    context = {'page': page}
    return render(request, 'base/sch_list.html', context=context)


def contact_us_page(request):
<<<<<<< HEAD
    return render(request, 'base/contact_us.html')


=======
    page = 'contact_us'
    context = {'page': page}
    return render(request, 'base/contact.html', context=context)
>>>>>>> 5699b0318966699833da87fd12656567cf0565a9
