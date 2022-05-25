from django.db.models.signals import post_save
from django.db.models import Avg
from django.dispatch import receiver
from .models import Rating, Product
 
 
@receiver(post_save, sender=Rating)
def calc_rating(sender, instance, created, **kwargs):
    if created:
        the_product = instance.product
        rating =  instance.product.rating_set.aggregate(Avg('rating')).get('rating__avg')
        the_product.average_rating = rating
        the_product.save()
        