from django.shortcuts import render
# Create your views here.
from .models import Hotel,Room

def signuppage(request):
    return render(request,"signup.html")

def hotellogin(request):
    return render(request,"login.html")
def loginadmin(request):
    if (request.method == "POST"):
        hotel=Hotel.objects.all()
        email = request.POST.get("email")
        pwd = request.POST.get("pwd")
        
        if email != None :
            hotel=Hotel.objects.get(email=email)
            if(hotel.password == pwd):
                data={
                    'hotel' : hotel
                }
                return render(request,"about.html",data)
    data={
        'msg' : "Wrong id or password"
    }
    return render(request,"login.html",data)

def hotellist(request):
    if (request.method == "POST"):
        Rooms = Room.objects.all()
        checkin = request.POST.get("ckeckin")
        checkout = request.POST.get("ckeckout")
    rooms = Rooms.objects.filter(checkindate_lte=checkin)
    fRooms = rooms.objects.filter(checkoutdate_gte=checkin)
    hotel=Hotel.objects.all(Hotelid=fRooms.Hotelid)
    
    data={
        'hotel' : hotel
    }
    return render(request,"test.html",data)

def about(request):
    
    return render(request,"about.html")