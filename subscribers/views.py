from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail

from .models import Subscribers


def subscribers(request):
    """ subscribe form view """
    subscribers_form = SubscribersForm(request.POST or None)
    if request.method == "POST":

        if subscribers_form.is_valid():
            print("Form is valid")
            subscribers_form.save()
            send_mail(
                'Thank you for subscribing',
                request.POST.get('message'),
                settings.DEFAULT_FROM_EMAIL,
                [request.POST.get('email')],
                fail_silently=False,
            )
            messages.success(
                request,
                'Thank you!'
                )
            return redirect('subscribers')
    context = {
        'form': subscribers_form,
    }

    return render(request, 'subscribers/subscribers.html', context)
