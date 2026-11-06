from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.IntegerField()
    category = models.CharField(max_length=50)
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='books/', blank=True, null=True)

    def __str__(self):
        return self.title