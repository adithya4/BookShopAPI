from django.db import models
from uuid import uuid4
# Create your models here.
class Collection(models.Model):
    collection_type = models.CharField(max_length=50)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.collection_type

class Books(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=30)
    description = models.TextField()
    collection = models.ForeignKey(Collection, on_delete= models.CASCADE, related_name="books")

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.title
    
class Carts(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Carts, on_delete=models.CASCADE, related_name='items')
    book = models.ForeignKey(Books,on_delete=models.CASCADE)

    class Meta:
        unique_together = [['cart','book']]

    def __str__(self):
        return str(self.cart)