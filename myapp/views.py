from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, request




def functioncontact(request):

    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]   
        subject = request.POST["subject"] + " " + name
        message = request.POST["message"]

        try:
            send_mail(
            subject, 
            message,
            email, 
            ['elfirdoussimohamed99@gmail.com'],
            fail_silently=False,
            )
        except BadHeaderError:
            return HttpResponse('Invalid header found')
        return render(request, 'myapp/functioncontact.html', {'name':subject})
    return render(request, 'myapp/functioncontact.html')
