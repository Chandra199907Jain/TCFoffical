from django.db import models

# Create your models here.
class Register(models.Model):
    name= models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class Category(models.Model):
    category_name=models.CharField(max_length=100)

class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    product_name=models.CharField(max_length=200)
    product_desc=models.CharField(max_length = 500)
    product_image=models.ImageField()
    product_price=models.IntegerField(default=0)

class Order(models.Model):
    address=models.CharField(max_length = 1000)
    zip_code=models.CharField(max_length = 200)
    customer=models.ForeignKey(Register,on_delete=models.CASCADE,default=1)
    contact = models.IntegerField(default=1)

class Cart(models.Model):
    size=models.CharField(max_length=100)
    quantity=models.IntegerField(default=1)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    orders=models.ForeignKey(Order,on_delete=models.CASCADE,default=1)



