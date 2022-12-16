from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages


from .forms import NewsletterForm
from .models import Newsletter


def newsletter(request):
    """ Newsletter form view """
    newsletter_form = NewsletterForm(request.POST or None)
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
                'Thank you for subscribing '
                'We will send you monthly updates, news and special offers'
                )
            return redirect('newsletter')
    context = {
        'form': newsletter_form,
    }

    return render(request, 'newsletter/newsletter.html', context)
