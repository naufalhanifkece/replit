from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Book


# Create your views here.
def index(request):
  context = {'book_list': Book.objects.all()}
  return render(request, "books/index.html", context)


def add(request):
  return render(request, "books/form.html")


def save(request):
  buku = Book(
      judul=request.POST['judul'],
      publish=request.POST['publish'],
  )
  buku.save()

  return HttpResponseRedirect(reverse('books.index'))


def delete(request, book_id):
  buku = get_object_or_404(Book, pk=book_id)
  buku.delete()
  return HttpResponseRedirect(reverse('books.index'))

def edit(request, book_id):
  buku = get_object_or_404(Book, pk=book_id)
  publish = buku.publish.date()
  context = {
    'id': book_id,
    'judul': buku.judul,
    'publish': publish.strftime('%Y-%m-%d'),
  }
  return render(request, "books/form_edit.html", context)

def update(request, book_id):
  buku = get_object_or_404(Book, pk=book_id)
  buku.judul = request.POST['judul']
  buku.publish = request.POST['publish']
  buku.save()

  return HttpResponseRedirect(reverse('books.index'))