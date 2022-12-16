from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages


from .forms import ContactForm
from .models import Contact


def contact(request):
    """ Contact form view """
    contact_form = ContactForm(request.POST or None)
    if request.method == "POST":

        if contact_form.is_valid():
            print("Form is valid")
            contact_form.save()
            send_mail(
                'Thank you for contacting FitSpace',
                request.POST.get('message'),
                settings.DEFAULT_FROM_EMAIL,
                [request.POST.get('email')],
                fail_silently=False,
            )
            messages.success(
                request,
                'Thank you for your message. '
                'We aim to get back to you within 48 hours.'
                )
            return redirect('contact')
    context = {
        'form': contact_form,
    }

    return render(request, 'contact/contact.html', context)
