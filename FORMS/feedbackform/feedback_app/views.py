from django.shortcuts import render

# Create your views here.
from .forms import FeedbackForm
def feedback_form(request):
    if request.method =='POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            return render(request, 'thankyou.html')
    else:
        form = FeedbackForm()
    return render(request, 'feedback_form.html',{'form':form})