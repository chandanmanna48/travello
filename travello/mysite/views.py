from django.shortcuts import render
from django.http import HttpResponse
from .models import update


# Create your views here.
def index(request):

    obj1=update()
    obj1.name="Bhubaneswar"
    obj1.price=800
    obj1.desc="It is famous as a temple city"
    obj1.offer=True
    obj1.image='destination_4.jpg'

    obj2=update()
    obj2.name="Cuttack"
    obj2.price=600
    obj2.desc="It is famous as a temple city"
    obj2.offer=False
    obj2.image='destination_5.jpg'

    obj3=update()
    obj3.name="Balasore"
    obj3.price=400
    obj3.desc="It is famous as a temple city"
    obj3.offer=True
    obj3.image='destination_6.jpg'

    #objs=[obj1,obj2,obj3]
    objs=update.objects.all()
    return render(request,'index.html',{'objs':objs})
