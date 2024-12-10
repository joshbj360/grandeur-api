from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class GUser(AbstractUser):
    # General fields for all users
    email = models.EmailField(unique=True)
    is_verified = models.BooleanField(default=False)  # KYC flag
    is_seller = models.BooleanField(default=False)  # User's seller status
    
    # Reputation score for hybrid ranking system
    reputation_score = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    
    # Engagement score
    engagement_score = models.DecimalField(max_digits=2, decimal_places=2,default=0.00)

    def __str__(self):
        return self.username
