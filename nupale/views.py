from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_page
from django.core.mail import send_mail

from .forms import *


# Create your views here.


def index(request):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Extract form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            
            # Prepare email content
            email_subject = f"Contact Form Submission: {subject}"
            email_body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
            
            # Send email using Django's send_mail function
            send_mail(
                email_subject,
                email_body,
                email,  # From address (user's email)
                ['contact@nupale.com'],  # To address (your email)
                fail_silently=False,
            )
            
            # Redirect to a success page
            return redirect('contact_success')
    
    context = {
        'form': form,
    }

    return render(request, 'website/index.html', context)






@cache_page(60 * 5)
def services(request):
    return render(request, 'website/services.html')




 

def career(request):
    return render(request, 'website/careers.html')







def about(request):
    return render(request, 'website/about.html')





def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Extract form data
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data.get('phone_number')
            address = form.cleaned_data.get('address')
            message = form.cleaned_data['message']
            
            # Compose email
            email_subject = f"Contact Form Submission: {subject}"
            email_message = (
                f"Name: {first_name} {last_name}\n"
                f"Email: {email}\n"
                f"Phone: {phone_number}\n"
                f"Address: {address}\n\n"
                f"Message:\n{message}"
            )
            email_from = email  # Reply to the sender
            recipient_list = ['your_outlook_email@example.com']
            
            # Send email
            send_mail(email_subject, email_message, email_from, recipient_list)
            
            return render(request, 'contact_success.html')  # Redirect or render a success page

    else:
        form = ContactForm()
    
    context = {
        'form': form,
    }

    return render(request, 'website/contact.html', context)




#@cache_page(60 * 5)
def quote(request):
    if request.method == 'POST':
        form = QuoteCreationForm(request.POST)
        if form.is_valid():
            # Extract form data
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data.get('phone_number')
            address = form.cleaned_data.get('address')
            description = form.cleaned_data['description']
            
            # Compose email
            email_subject = f"Contact Form Submission: {subject}"
            email_message = (
                f"Name: {first_name} {last_name}\n"
                f"Email: {email}\n"
                f"Phone: {phone_number}\n"
                f"Address: {address}\n\n"
                f"Description:\n{description}"
            )
            email_from = email  # Reply to the sender
            recipient_list = ['your_outlook_email@example.com']
            
            # Send email
            send_mail(email_subject, email_message, email_from, recipient_list)
            
            return render(request, 'contact_success.html')  # Redirect or render a success page

    else:
        form = QuoteCreationForm()
    
    context = {
        'form': form,
    }

    return render(request, 'website/quote_request.html', context)



#@cache_page(60 * 5)
def privacy_policy(request):
    return render(request, 'website/privacy_policy.html')




#@cache_page(60 * 5)
def terms(request):
    return render(request, 'website/terms.html')

