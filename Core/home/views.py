from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator
from LMS.models import Book
from accounts.models import Profile
# Create your views here.

def index(request):
    profile = get_object_or_404(Profile,user=request.user)
    newBooks=Book.objects.all()[:4]
    return render(request,'home/index.html',{"newBooks":newBooks,"profile":profile})


def bookDetails(request ,id ):
    book=get_object_or_404(Book,id=id)
    return render(request,"home/bookDetail.html",{"book":book})

def books(request):
    books=Book.objects.all()
    paginator = Paginator(books, 10)
    page_number=request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request,"home/books.html",{"books":page_obj})