from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Category(models.Model):
    name = models.CharField(max_length=32)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return f"{self.name}"


class Listing(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    title = models.CharField(max_length=1000)
    description = models.TextField(max_length=1000)
    image = models.URLField(null=True, blank=True, max_length=250)
    starting_price = models.DecimalField(
        decimal_places=2, max_digits=10, default=1.00)
    current_price = models.DecimalField(
        decimal_places=2, max_digits=10, default=0.00)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)
    is_active = models.BooleanField(default=True)


class Bid(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, related_name='bids')
    item = models.ForeignKey(Listing, on_delete=models.CASCADE, null=True)
    bid_amount = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return f"{self.user}'s bid on {self.item} is {self.bid_amount}"


class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    item = models.ForeignKey(Listing, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.item}"


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    item = models.ForeignKey(Listing, on_delete=models.CASCADE, null=True)
    content = models.TextField(max_length=1200, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"{self.content}"
