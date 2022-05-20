from django.db import models
from myaccount.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    slug =models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    made_in = models.CharField(max_length=15)
    image = models.ImageField(upload_to='products_image')

    def __str__(self):
        return self.name
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = self.name.lower().replace(' ', '-')
        return super().save(force_insert, force_update, using, update_fields)

class Like(models.Model):
    user = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='likes', on_delete=models.CASCADE)

class Comment(models.Model):
    user = models.ForeignKey(User, related_name='comments',on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField()



