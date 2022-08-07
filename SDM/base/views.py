from cgitb import html
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail
from django.template.loader import render_to_string

# Create your views here.

def landing_page(request):
    return render(request, 'base/landing.html')

def school_reg_page(request):
    return render(request, 'base/school_reg_with_us.html')

def contact_us_page(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            html = render_to_string('base/contact/contact_us_form.html', {
                'name': name,
                'email': email,
                'message': message
            })

            send_mail('Contact Us', 'We have been contacted', 'moshopeowo@gmail.com', ['moshopeowo@gmail.com'], html_message=html)

            return redirect('index')

    else:
        form = ContactForm()


    return render(request, 'base/contact/index.html', {
        'form': form})

