from django.db import models
from shopapp.models import Product


class Cart(models.Model):
    cart_id=models.CharField(max_length=250,blank=True,null=True)
    date_added=models.DateField(auto_now_add=True,null=True)
    
    class Meta:
        db_table='Cart'
        ordering=['date_added']
        
    def __str__(self):
        return '{}'.format (self.cart_id)
    
class CartItem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE,null=True)
    quantity=models.IntegerField(null=True)
    active=models.BooleanField(default=True,null=True)
    class Meta:
        db_table='CartItem'
    def sub_total(self):
        return self.product.price * self.quantity
    
    def __str__(self):
        return '{}'.format (self.product)
    
        
