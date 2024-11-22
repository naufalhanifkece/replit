from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {'title': "Aplikasi CRUD Penyimpanan Catatan Sederhana"}
    return render(request, 'index.html', context)


# Create your views here.
