from django.shortcuts import render

# Create your views here.
from .forms import ExmRegistrationForm 

def exam_registration(request):
    if request.method == 'POST':
        form = ExmRegistrationForm(request.POST , request.FILES)
        if form.is_valid():
            #print form.
            print(form.cleaned_data)
            return redirect('sucess')
    else:
        form = ExmRegistrationForm()
        return render(request, "exam_registration.html" , {'form':form})

def sucess(request):
    return render(request, "sucess.html")