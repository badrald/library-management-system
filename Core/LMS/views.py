from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Sum
from .models import *
from .forms import *

# Create your views here.
@staff_member_required
def Index(request):
    if request.method == 'POST':
        add_book=BookForm(request.POST, request.FILES)
        if add_book.is_valid():
            add_book.save()
            return redirect('/mangement')
        add_cat=CategoryForm(request.POST)
        if add_cat.is_valid():
            add_cat.save()
            add_cat=CategoryForm()
    context = {
        'Books':Book.objects.all(),
        'Categories':Category.objects.all(),
        'form': BookForm(),
        'catform':CategoryForm(),
        'allBooks': Book.objects.filter(active=True).aggregate(Sum("amount"))["amount__sum"],
        'bookava':Book.objects.filter(status='available').count(),
        'bookre':Book.objects.filter(status='retailed').count(),
        'bookso':Book.objects.filter(status='sold').count(),
        
        }
    return render(request,'LMS/Pages/index.html',context)
@staff_member_required
def Books(request):
    search =Book.objects.all();
    title= None
    if "search_name" in request.GET:
        title = request.GET["search_name"]
        if title:
            search = search.filter(title__icontains=title)

    context = {
        'Books':search,
        'Categories':Category.objects.all(),
        'form': BookForm(),
        'catform':CategoryForm(),
        }
    return render(request,"LMS/Pages/books.html",context)

@staff_member_required
def update(request,id):
    book_id=Book.objects.get(id=id)
    if request.method == 'POST':
        book_save=BookForm(request.POST , request.FILES , instance=book_id )
        if book_save.is_valid():
            book_save.save()
            return redirect('/mangement')
    else:
        book_save=BookForm(instance=book_id)
    context = {
        'bookform': book_save,
        }
    return render(request,"LMS/Pages/update.html",context)
@staff_member_required
def delete(request,id):
    book_del=get_object_or_404(Book,id=id)
    if request.method == 'POST':
        book_del.delete()
        return redirect('/mangement')
    return render(request,'LMS/Pages/delete.html')