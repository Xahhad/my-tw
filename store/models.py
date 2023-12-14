from django.db import models
import datetime

class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Customer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=7)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=250, default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/product/')
    #Adding sale stuff:
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0, decimal_places=2, max_digits=7)

    def __str__(self):
        return self.name
    

class Order(models.Model):
    product = models.ForeignKey(Product, models.CASCADE)
    customer = models.ForeignKey(Customer, models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=200, default= '', blank= '')
    phone = models.CharField(max_length=20, default= '', blank= '')
    date = models.DateField(default= datetime.datetime.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.product