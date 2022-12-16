from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail


from .models import Subscribe
from .forms import subscribe


def subscribe(request):
    """ subscribe form view """
    subscribe_form = Subscribe(request.POST or None)
    if request.method == "POST":

        if nsubscribe_form.is_valid():
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
                'Thank you!'
                )
            return redirect('newsletter')
    context = {
        'form': subscribe_form,
    }

    return render(request, 'subscribe/newsletter.html', context)
