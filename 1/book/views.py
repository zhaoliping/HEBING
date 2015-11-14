from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from models import Author,Book
from django.views.decorators.csrf import csrf_exempt


def index(request):
        books = Book.objects.all()
        if request.method == 'GET':
                if 'delete' in request.GET and request.GET['delete']:
                        ISBN = request.GET['delete']
                        book = Book.objects.filter(ISBN = ISBN)
                        book.delete()
                        books = Book.objects.all()
        return render_to_response('index.html',{'books':books})


def search(request):
        if request.method == 'GET':
                if 'name' in request.GET and request.GET['name']:
                        
                                author = Author.objects.get(Name = name)
                                books = author.book_set.all()
                                return render_to_response('search.html',{'author':author,'books':books})
                        error = "not exist!"
                        return render_to_response('search.html',{'error':error})
                error = "Please input a name"
                return render_to_response('search.html',{'error':error})
	return render_to_response('search.html')


def book(request,i):
        ISBN = i
        s = Book.objects.filter(ISBN = ISBN)
        if s:
                book = Book.objects.get(ISBN = ISBN)
                return render_to_response('book.html',{'book':book})
        return render_to_response('book.html')

@csrf_exempt
def update(request,i):
        authors = Author.objects.all()
        ISBN = i
        book = Book.objects.get(ISBN = i)
        if request.method == 'POST':
                ISBN = i
                book = Book.objects.get(ISBN = i)
                s = Author.objects.filter(Name = request.POST['AuthorID'])
                if s:
                        book.AuthorID = Author.objects.get(Name = request.POST['AuthorID'])
                        book.Publisher = request.POST['publisher']
                        book.PublishDate = request.POST['publishdate']
                        book.Price = request.POST['price']
                        book.save()
        return render_to_response('update.html',{'authors':authors,'book':book})


@csrf_exempt
def addbook(request):
        authors = Author.objects.all()
	if request.method == 'POST':
                ISBN = request.POST['isbn']
                Title = request.POST['title']
                Publisher = request.POST['publisher']
                PublishDate = request.POST['publishdate']
                Price = request.POST['price']
                AuthorID = Author.objects.get(Name = request.POST['AuthorID'])
                book = Book.objects.create(ISBN = ISBN,Title = Title,AuthorID = AuthorID,Publisher = Publisher,
                                                   PublishDate = PublishDate,Price = Price)
                book.save()
                return HttpResponseRedirect('/index')
        authors = Author.objects.all()
        return render_to_response('addbook.html',{'authors':authors})

@csrf_exempt
def addauthor(request,option = "none"):
        if request.method == 'POST':
            AuthorID = request.POST['authorid']
            Name = request.POST['name']
            Age = request.POST['age']
            Country = request.POST['country']
            author = Author.objects.create(AuthorID = AuthorID,Name = Name,Age = Age,Country = Country)
            author.save()
            return HttpResponseRedirect('/index')
        return  render_to_response('addauthor.html')
