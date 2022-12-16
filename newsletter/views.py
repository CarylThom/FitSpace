from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail


from .models import Newsletter


def newsletter(request):
    """ subscribe form view """
    newsletter_form = Newsletter(request.POST or None)
    if request.method == "POST":

        if newsletter_form.is_valid():
            print("Form is valid")
            newsletter_form.save()
            send_mail(
                'Thank you for subscribing to our newsletter',
                request.POST.get('message'),
                settings.DEFAULT_FROM_EMAIL,
                [request.POST.get('email')],
                fail_silently=False,
            )
            messages.success(
                request,
                'Thank you!'
                )
            return redirect('newsletter')
    context = {
        'form': newsletter_form,
    }

    return render(request, 'newsletter/newsletter.html', context)
