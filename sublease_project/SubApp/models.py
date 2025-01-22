from django.db import models

class Sublease(models.Model):

    address = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=10)

    # Lease details
    rent = models.DecimalField(max_digits=7, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()

    # Contact information
    contact_name = models.CharField(max_length=100)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=15, blank=True, null=True)

    # Property details
    property_type = models.CharField(max_length=50, choices=[
        ('Apartment', 'Apartment'),
        ('House', 'House'),
        ('Studio', 'Studio'),
        ('Other', 'Other'),
    ])
    bedrooms = models.PositiveIntegerField(default=1)
    bathrooms = models.PositiveIntegerField(default=1)
    furnished = models.BooleanField(default=False)
    amenities = models.TextField(blank=True, null=True)  # E.g., "Gym, Pool, Parking"

    # Availability status
    is_available = models.BooleanField(default=True)

    # Images
    image = models.ImageField(upload_to='sublease_images/', blank=True, null=True)

    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.address},{self.postal_code} - ${self.rent}/month"

