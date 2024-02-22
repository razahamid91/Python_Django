from django.shortcuts import render

# Create your views here.
def home(request):
    #data
    book1={"title":"book1","author":"author1", "subject":"fiction" }
    book2={"title":"book2","author":"author2", "subject":"science" }
    context={
        "book1":book1, 
        "book2":book2,
        }
    return render(request,'home.html',context)

def about(request):
    return  render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def books(request):
    books=[
    {"title":"book1","author":"author1", "subject":"fiction" },
    {"title":"book2","author":"author2", "subject":"fiction" },
    {"title":"book3","author":"author3", "subject":"fiction" },
    {"title":"book4","author":"author4", "subject":"fiction" },
    ]
    return render(request,'books.html')
