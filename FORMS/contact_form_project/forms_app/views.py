from django.shortcuts import render

# Create your views here.

from .form import ContactForm

def contact_form(request):
    if request.method =='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
                #process the form data (send email , save the deaft)

                print(form.cleaned_data)
                return render(request , "thankyou_form.html")
    else:
        form = ContactForm()
        return render(request , "contact_form.html",{'form':form})

def thankyou_form(request):
    return render(request, "thankyou_form.html")
