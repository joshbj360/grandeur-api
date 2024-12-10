from django.contrib import admin

from .models import SellerProfile, SellerReview

# Register your models here.
admin.site.register(SellerProfile)
admin.site.register(SellerReview)