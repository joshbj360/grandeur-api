from django.db import models

from grandeur.apps.GUser.models import GUser

# Create your models here.
class SellerProfile(models.Model):
    seller = models.OneToOneField(
        GUser,
        on_delete=models.CASCADE,
        related_name='seller_profile'
    )
    store_name = models.CharField(max_length=255)
    business_description = models.TextField(blank=True, null=True)
    verified_seller = models.BooleanField(default=False)  # Verified seller flag
    
    # Additional seller-specific fields
    tax_id = models.CharField(max_length=50, blank=True, null=True)  # Optional
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Store"


class SellerReview(models.Model):
    seller = models.ForeignKey(
        GUser,
        on_delete=models.CASCADE,
        related_name='seller_reviews'
    )
    buyer = models.ForeignKey(
        GUser,
        on_delete=models.SET_NULL,
        null=True, 
        related_name='given_reviews'
    )
    rating = models.PositiveIntegerField()  # e.g., 1-5
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.seller.username} by {self.buyer.username}"


class KYC(models.Model):
    user = models.OneToOneField(
        GUser,
        on_delete=models.CASCADE,
        related_name='kyc'
    )
    document_type = models.CharField(max_length=50)  # e.g., ID, Passport
    document_file = models.FileField(upload_to='kyc_documents/')
    is_verified = models.BooleanField(default=False)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"KYC for {self.user.username}"
