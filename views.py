from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
    return render(request, 'galleryHome.html', {})

def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        # send an email
        send_mail(
            message_name, #subject
            message, #messsage
            message_email, #from Email
            ['kamiem62@gmail.com'], #to email


        )


        return render(request, 'galleryContact.html'), {'message_name' : message_name}

else:
    return render(request, 'contact.html', {})
