from django.shortcuts import render

# Create your views here.

def custom_404(request):
    return render(request , "404.html")
from django.http import HttpResponseNotFound

def sucessful(request):
    return HTTPResponseNotFound("sucessful", status = 200)
     
def created(request):
    return HttpResponseNotFound("created successfully", status =201)

def accepted(request):
    return HttpResponseNotFound("accepted successfully", status =202)

def non_authorization(request):
    return HttpResponseNotFound("non-authorization", status =203)

def found(request):
    return HttpResponseNotFound("found", status =302)

def bad_request(request):
    return HttpResponseNotFound("bad request", status =400)


