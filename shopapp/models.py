from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=200,unique=True)
    slug=models.SlugField(max_length=200,unique=True)
    des=models.TextField(blank=True)
    image=models.ImageField(upload_to='category',blank=True)
    
    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'
        
    def get_url(self):
        return reverse('shopapp:products_by_category',args=[self.slug])
    
    def __str__(self):
        return '{}'.format(self.name)
    
class Product(models.Model):
        category=models.ForeignKey(Category,on_delete=models.CASCADE)
        name=models.CharField(max_length=200,unique=True)
        slug=models.SlugField(max_length=200,unique=True)
        des=models.TextField(blank=True)
        image=models.ImageField(upload_to='product',blank=True)
        price=models.DecimalField(max_digits=10,decimal_places=2)
        stock=models.IntegerField()
        available=models.BooleanField(default=True)
        created=models.DateTimeField(auto_now_add=True)
        updated=models.DateTimeField(auto_now=True)
        
        def get_url(self):
            return reverse('shopapp:prodCatdetail',args=[self.category.slug,self.slug])
        
        class Meta:
            ordering=('name',)
            verbose_name='product'
            verbose_name_plural='products'
            
        def __str__(self):
            return '{}'.format(self.name)
    
        
    