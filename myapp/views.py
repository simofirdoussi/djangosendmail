from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, request
from django.views.generic import FormView
from .forms import Sendit



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



class ContactFormView(FormView):
    template_name = 'myapp/classcontact.html'
    form_class = Sendit
    success_url = 'classcontact/'

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        email=form.cleaned_data.get('email')
        subject = form.cleaned_data.get('subject')
        message = form.cleaned_data.get('message')
        send_mail(
            subject, 
            message,
            email, 
            ['elfirdoussimohamed99@gmail.com'],
            fail_silently=False)

        return super(ContactFormView, self).form_valid(form)

