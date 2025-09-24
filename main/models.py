from django.db import models
from django.contrib.auth.models import User
import uuid

class Product(models.Model):
    CATEGORY_CHOICES = [
        ("jersey", "Jersey"),
        ("celana", "Celana"),
        ("sarung_tangan", "Sarung Tangan"),
        ("sepatu", "Sepatu"),
        ("pelindung", "Pelindung (siku/lutut/pinggul)"),
        ("kaos_kaki", "Kaos Kaki"),
        ("aksesoris", "Aksesoris"),
    ]
    
    SIZE_CHOICES = [
        ('xs', 'XS'),
        ('s', 'S'),
        ('m', 'M'),
        ('l', 'L'),
        ('xl', 'XL'),
        ('xxl', 'XXL'),
        ('xxxl', 'XXXL'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='jersey')
    thumbnail = models.URLField()
    price = models.IntegerField()
    stock = models.IntegerField(blank=True, null=True)
    size = models.CharField(max_length=20,  choices=SIZE_CHOICES, default='l')    
    product_views = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    @property
    def is_product_trending(self):
        return self.product_views > 20
        
    def increment_views(self):
        self.product_views += 1
        self.save()