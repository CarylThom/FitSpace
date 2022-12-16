from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from django import forms
from .models import Subscribe


def subscribe(request):
    """ Subscribe form view """
    subscribe_form = Subscribe(request.POST or None)
    if request.method == "POST":

        if subscribe_form.is_valid():
            print("Form is valid")
            subscribe_form.save()
            send_mail(
                'Thank you for subscribing to our newsletter',
                request.POST.get('message'),
                settings.DEFAULT_FROM_EMAIL,
                [request.POST.get('email')],
                fail_silently=False,
            )
            messages.success(
                request,
                'Thank you for subscribing to our newsletter. '
                'We will send you our monthly news and special offers '
                )
            return redirect('subscribe')
    context = {
        'form': subscribe_form,
    }

    return render(request, 'subscribe/subscribe.html', context)
