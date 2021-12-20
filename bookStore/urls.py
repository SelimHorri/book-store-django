
from django.urls.resolvers import URLPattern
from .views import index,getBookDetails
from django.urls import path

urlpatterns=[
    path("",index,name='index'),
    path("<int:book_id>/",getBookDetails,name='getBookDetails')
]