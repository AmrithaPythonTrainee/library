from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Book


# Create your views here.

def index(request):
    books=Book.objects.all()
    return render(request,"viewbook.html",{"books":books})
def index1(request):
    return render(request,"loginandregister.html")

def addBookView(request):
    return render(request,"addbook.html")
def addBook(request):
    if request.method=="POST":
        t=request.POST["title"]
        p=request.POST["price"]
        l=request.POST["lang"]
        a=request.POST["author"]
        print(t,p,l,a)
        book=Book()
        book.title=t
        book.price=p
        book.lang=l
        book.author=a
        book.save()
        return HttpResponseRedirect('/')
def editBook(request):
    if request.method=="POST":
        t=request.POST["title"]
        p=request.POST["price"]
        l=request.POST["lang"]
        a=request.POST["author"]
        book=Book.objects.get(id=request.POST['bid'])
        book.title=t
        book.price=p
        book.lang=l
        book.author=a
        book.save()
        return HttpResponseRedirect('/')

def editBookView(request):
    book=Book.objects.get(id=request.GET['bookid'])
    return render(request,"edit-book.html",{"book":book})

def deleteBookView(request):
      book=Book.objects.get(id=request.GET['bookid'])
      book.delete()
      return HttpResponseRedirect('/')