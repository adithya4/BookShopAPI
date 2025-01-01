from django.db import models

# Create your models here.
class Collection(models.Model):
    collection_type = models.CharField(max_length=50)

    def __str__(self):
        return self.collection_type

class Books(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=30)
    description = models.TextField()
    collection = models.ForeignKey(Collection, on_delete= models.CASCADE, related_name="books")

    def __str__(self):
        return self.title