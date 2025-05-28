from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STATE_CHOICE = (
    ("Andhra Pradesh", "Andhra Pradesh"),
    ("Arunachal Pradesh", "Arunachal Pradesh"),
    ("Assam", "Assam"),
    ("Bihar", "Bihar"),
    ("Chhattisgarh", "Chhattisgarh"),
    ("Goa", "Goa"),
    ("Gujarat", "Gujarat"),
    ("Haryana", "Haryana"),
    ("Himachal Pradesh", "Himachal Pradesh"),
    ("Jharkhand", "Jharkhand"),
    ("Karnataka", "Karnataka"),
    ("Kerala", "Kerala"),
    ("Madhya Pradesh", "Madhya Pradesh"),
    ("Maharashtra", "Maharashtra"),
    ("Manipur", "Manipur"),
    ("Meghalaya", "Meghalaya"),
    ("Mizoram", "Mizoram"),
    ("Nagaland", "Nagaland"),
    ("Odisha", "Odisha"),
    ("Punjab", "Punjab"),
    ("Rajasthan", "Rajasthan"),
    ("Sikkim", "Sikkim"),
    ("Tamil Nadu", "Tamil Nadu"),
    ("Telangana", "Telangana"),
    ("Tripura", "Tripura"),
    ("Uttar Pradesh", "Uttar Pradesh"),
    ("Uttarakhand", "Uttarakhand"),
    ("West Bengal", "West Bengal")
)


CATEGORY = (
    ("M" , "Men's Fashion"),
    ("W" , "Women's Fashion"),
    ("Sh" , "Shoes"),
    ("SG" , "Sunglass"),
    ("C" , "Camera")
)

STATUS = (
    ("Accepted" , "Accepted"),
    ("On the way" , "On the way"),
    ("Delivered" , "Delivered"),
    ("Cancelled" , "Cancelled")
)


class Customer(models.Model):
    user =  models.ForeignKey(User ,on_delete=models.CASCADE)
    name =  models.CharField( max_length = 100)
    locality = models.CharField( max_length=200)
    city =  models.CharField( max_length=150)
    # zipcode = models.IntegerField()
    # state =  models.CharField( choices = STATE_CHOICE, max_length = 50)

    def __str__(self):
        return str(self.User)

class Product(models.Model):
    p_name = models.CharField(max_length = 250)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    discription =  models.TextField()
    category = models.CharField(choices = CATEGORY , max_length = 20)
    barnd = models.CharField(max_length = 250)
    image = models.ImageField(upload_to = 'prd_img' )

    def __str__(self):
        return self.p_name

class Cart(models.Model):
    user =  models.ForeignKey(User,on_delete=models.CASCADE)
    product =  models.ForeignKey(Product ,on_delete=models.CASCADE)
    quantity =  models.PositiveIntegerField( default = 1)

    def __str__(self):
        return  str(self.pk)

class OrderPlaced(models.Model):
    customer =  models.ForeignKey(Customer ,on_delete=models.CASCADE)
    product =  models.ForeignKey(Product ,on_delete=models.CASCADE)
    cart =  models.ForeignKey(Cart ,on_delete=models.CASCADE , null= True)
    quantity =  models.PositiveIntegerField()
    order_date = models.DateField ( auto_now_add = True)
    status = models.CharField (choices = STATUS , max_length = 10)

    def __str__(self):
        return self.pk
    
    
