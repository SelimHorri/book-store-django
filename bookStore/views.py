
from django.shortcuts import render
from django.http import HttpResponse
from .models import Book


def index(request):
    result=Book.objects.all()
    context={"listofbooks":result}
    return render(request,'GestionLivre/Book_Liste.html',context)

def getBookDetails(request,article_id):
    result=Book.objects.get(pk=article_id)
    context={"listofbooks":result}
    return render(request,'GestionLivre/Book_details.html',context)



