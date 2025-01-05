from rest_framework import serializers
from .models import Books, Collection, Carts, CartItem
class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ['id', 'title', 'author', 'description','collection']

class CollectionSerializer(serializers.Serializer):
    
    books = serializers.SerializerMethodField(method_name="books_list")

    def books_list(self, collection:Collection):
        return collection.books.all()

class CartItemSerializer(serializers.ModelSerializer):
    # Include the book details directly using the related `Books` serializer
    book_details = serializers.SerializerMethodField(method_name='get_book_details')

    def get_book_details(self, cart_item):
        # Access the book details through the foreign key relationship
        book = cart_item.book
        return {
            "id": book.id,
            "title": book.title,
            "author": book.author,
            "description": book.description,
            "collection": book.collection.collection_type  # Assuming you want the collection type
        }

    class Meta:
        model = CartItem
        fields = ['id', 'book_details']  # Add 'book_details' to the serialized fields


class CartSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    items = CartItemSerializer(many=True)
    class Meta:
        model = Carts
        fields=['id', 'items'] 
