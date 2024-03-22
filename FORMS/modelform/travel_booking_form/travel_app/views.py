from django.shortcuts import render

# Create your views here.

from .forms import BookingForm

def travel_booking(request):
    if request.method =='POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            return render(request, 'success.html')
        
    else:
        form=BookingForm()

    return render(request, 'bookingform.html', {'form':form})