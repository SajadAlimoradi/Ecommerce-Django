from django.db import models
from category.models import Category
from django.urls import reverse

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    slug         = models.SlugField(max_length=200, unique=True)
    price        = models.DecimalField(max_digits=10, decimal_places=2)
    description  = models.TextField(blank=True)
    cat_image    = models.ImageField(upload_to='photos/products', blank=True)
    stock        = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category     = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date= models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
    
    def get_url(self):
        return reverse('products_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.product_name