from django.db import models
# from account.models import MyUser

class Category(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    slug =models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    slug = models.SlugField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    made_in = models.CharField(max_length=15)
    image = models.ImageField(upload_to='furniture_image')

    def __str__(self):
        return self.name
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = self.name.lower().replace(' ', '-')
        return super().save(force_insert, force_update, using, update_fields)


