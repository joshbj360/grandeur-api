from django.db import models

from grandeur.apps.GUser.models import GUser


class Product(models.Model):
    seller = models.ForeignKey(
        GUser, 
        on_delete=models.CASCADE,
        related_name='products'
    )
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    category = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    is_approved = models.BooleanField(default=False)  # For moderation

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class ProductReview(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='product_reviews'
    )
    buyer = models.ForeignKey(
        GUser,
        on_delete=models.SET_NULL,
        null=True, 
        related_name='buyer_reviews'
    )
    rating = models.PositiveIntegerField()  # e.g., 1-5
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.product.name} by {self.buyer.username}"

