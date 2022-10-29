from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from .forms import ContactForm


def contact(request):
    """ Contact form view """
    contact_form = ContactForm
    if request.method == "POST":
        form_data = {
            'name': request.POST.get('name', ''),
            'email': request.POST.get('email', ''),
            'message': request.POST.get('message', '')
        }
        print(f"FORM_DATA: {form_data}")
        form = contact_form(form_data)

        if form.is_valid():
            print("Form is valid")
            send_mail(
                form_data['name'] + " - " + form_data['email'],
                form_data['message'],
                'fitspace@example.com',
                [settings.DEFAULT_FROM_EMAIL],
                fail_silently=False,
            )
        messages.success(
            request, 'Thank you for your message, we aim to get back to you within 2 working days.'
            )
        return redirect('contact')
    context = {
        'form': contact_form,
    }

    return render(request, 'contact/contact.html', context)
