from django.db import models

# Create your models here.

class Hotel(models.Model):
   Hotelid = models.AutoField
   name = models.CharField(max_length=100,null=True)
   address = models.CharField(max_length=200,null=True)
   phone_number = models.CharField(max_length=20,null=True)
   email = models.EmailField(null=True)
   images =  models.FileField(upload_to="Hotels",default="")
   password = models.CharField(max_length=10,null=True)
   
class Room(models.Model):
   Roomid = models.AutoField
   name = models.CharField(max_length=100,null=True)
   checkindate = models.DateField(null=False)
   checkoutdate = models.DateField(null=False)
   Hotelid= models.ForeignKey(Hotel,on_delete=models.CASCADE,null=True)
   
   
def __str__(self):
    return self.name 
