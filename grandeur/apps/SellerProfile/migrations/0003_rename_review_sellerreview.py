# Generated by Django 5.1.4 on 2024-12-10 17:30

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SellerProfile', '0002_kyc_review'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Review',
            new_name='SellerReview',
        ),
    ]