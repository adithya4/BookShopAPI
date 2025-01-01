from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination   
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .models import Books, Collection
from .serializers import BooksSerializer, CollectionSerializer
from django.http import JsonResponse, HttpResponse

# Create your views here.

class BookViewSet(ModelViewSet):
    queryset= Books.objects.all()
    serializer_class = BooksSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'description']
    ordering_fields = ['id', 'title']
    pagination_class = PageNumberPagination

#class CollectionViewSet(ReadOnlyModelViewSet):
#queryset = Collection.

@api_view()
def collection_list(request, id):
    collection = Collection.objects.get(id=id)
    books = collection.books.all()
    book_dict={}
    for i in range(len(books)):
        book_dict[books[i].id] = {
                   "title": books[i].title,
                    "author" : books[i].author,
                    "description" : books[i].description
                }
    print(book_dict)
    #queryset = collection.books.all()
    #serializer = CollectionSerializer(queryset, many=True)
    return JsonResponse(book_dict)
    