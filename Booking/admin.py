from django.contrib import admin
from Booking.models import Hotel,Room
# Register your models here.
 
class Adminhotel(admin.ModelAdmin):
    list_display =('Hotelid','name','address','phone_number','email','images')

class Adminroom(admin.ModelAdmin):
    list_display =('Roomid','name','checkindate','checkoutdate','Hotelid')

admin.site.register(Hotel,Adminhotel)
admin.site.register(Room,Adminroom)
