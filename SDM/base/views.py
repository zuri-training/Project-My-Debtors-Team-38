from cgitb import html
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail
from django.template.loader import render_to_string

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
    # page = 'contact_us'
    # context = {'page': page}
    # return render(request, 'base/contact.html', context=context)





    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            html = render_to_string('base/contact.html', {
                'name': name,
                'email': email,
                'message': message
            })

            send_mail('Contact Us', 'We have been contacted', 'moshopeowo@gmail.com', ['moshopeowo@gmail.com'], html_message=html)

            return redirect('index.html')

    else:
        form = ContactForm()


    return render(request, 'base/contact.html', {
        'form': form})
