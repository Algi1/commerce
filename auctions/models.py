from audioop import reverse
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Category(models.Model):
    """Category model will have name and description"""
    name = models.CharField(max_length=64)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.name

    class Meta:
        # Define metadata for the Category model
        verbose_name_plural = 'Categories'


class Listing(models.Model):
    """Listing model will have 
    title:
    starting_price:
    image: images to be uploaded via form and will be saved in media/images
    is_active: boolean
    seller: models.ForeignKey, user, on_delete=models.CASCADE, blank=True, null=True, related_name="user"
    category: models.ForeignKey, category, on_delete=models.CASCADE, blank=True, null=True, related_name="category_listings"""
    title = models.CharField(max_length=64)
    starting_price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images/')
    is_active = models.BooleanField(default=True)
    seller = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, related_name="user_listings")
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 blank=True, null=True, related_name="category_listings")

    def __str__(self):
        return self.title
