from django.db import models

# Create your models here.
class Product(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField()
    price=models.DecimalField(decimal_places=2)
    inventory=models.IntegerField()
    last_update=models.DateTimeField(auto_now=True)
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

    
    
