from rest_framework import serializers
from .models import Books, Collection
class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ['id', 'title', 'author', 'description','collection']

class CollectionSerializer(serializers.Serializer):
    
    books = serializers.SerializerMethodField(method_name="books_list")

    def books_list(self, collection:Collection):
        return collection.books.all()