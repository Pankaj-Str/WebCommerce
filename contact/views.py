from django.core.mail import send_mail
from django.shortcuts import render
from .forms import ContactForm
from django.conf import settings

# Create your views here.

def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():

        name = form.cleaned_data['name']
        comment = form.cleaned_data['comment']
        message = ''
        email_from = form.cleaned_data['email']
        email_to = [settings.EMAIL_HOST_USER]
        send_mail(
            'Subject here',
            'Here is the message.',
            'from@example.com',
            ['to@example.com'],
            fail_silently=False,
        )
    context = locals()
    template = './contact/contact.html'
    return render(request, template, context)
