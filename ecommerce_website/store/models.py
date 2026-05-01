from django.db import models

# Create your models here.
class Collection(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField()
   
    
class Product(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField()
    price=models.DecimalField(decimal_places=2)
    inventory=models.IntegerField()
    last_update=models.DateTimeField(auto_now=True)
     #a collection to have multiple products:ONE TO MANY RELATIONSHIP
    collection=models.ForeignKey(Collection,on_delete=models.PROTECT)
class Customer(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=100)
    birth_date=models.DateField(null=True)
class Order(models.Model):
    placed_at=models.DateTimeField(auto_now=True)

    #implementing choices
    PAYMENT_PENDING='P'
    PAYMENT_COMPLETED='C'
    PAYMENT_FAILED='F'
    PAYMENT_CHOICES=[
        'PAYMENT_PENDING','PENDING'
        'PAYMENT_FAILED','FAILED'
        'PAYMENT_COMPLETED','COMPLETED'
    ]
    payment_status=models.Choices(max_length=1,choices=PAYMENT_CHOICES,default=PAYMENT_PENDING)
    #a customer having multiple orders
    customer=models.ForeignKey(Customer,on_delete=models.PROTECT)

    
class Address(models.Model):
    street=models.CharField(max_length=255)
    city=models.CharField(max_length=255)

    #defining one-to -one relationship:a customer to have only one address
    customer=models.OneToOneField(Customer,on_delete=models.CASCADE,primary_key=True)

#DEFINING ONE TO MANY relationship:customer having multiple addresses
    # customer=models.ForeignKey(Customer,on_delete=models.CASCADE)

#other one-to-many relationships
class Cart(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    

class OrderItem(models.Model):
    # title=models.CharField(max_length=255)
    Product=models.ForeignKey(Product,on_delete=models.PROTECT)
    price=models.DecimalField(decimal_places=2)
    inventory=models.SmallIntegerField()
    #order having multiple items
    order=models.ForeignKey(Order,on_delete=models.PROTECT)
    cart=models.ForeignKey(Cart,on_delete=models.PROTECT)
class CartItem(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveSmallIntegerField()









