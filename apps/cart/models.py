from django.db import models
from datetime import datetime
from apps.loja.models import Loja
# Create your models here.



class Cart(models.Model):
    cart_id = models.CharField(max_length=100,blank=True)
    date_add = models.DateTimeField(default=datetime.now,blank=True)



    def __str__(self):
        return self.cart_id



class CartItem(models.Model):
    produto = models.ForeignKey(Loja,on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    active = models.BooleanField(default=True)


    def sub_total(self):
        return self.produto.preco * self.quantity


    def __str__(self):
        return self.produto


