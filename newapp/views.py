from django.shortcuts import render
from .models import *
# Create your views here.

def service(request):
    return render(request,'service.html')
def servicedetails(request):
    return render(request,'service-details.html')
def servicedetails2(request):
    return render(request,'service-details-2.html')

def index(request):
    return render(request,'index.html')

def blog(request):
    return render(request,'category.html')

def blogdetails(request):
    return render(request,'blog-details.html')

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def gallery(request):
    return render(request,'gallery.html')

def fetchformdata(request):
    useremail =request.POST.get("email")
    usermesssage = request.POST.get("message")
    newdata =timedelivery(email=useremail , message = usermesssage)
    newdata.save()
    return render(request,'service-details.html')

def fetchdata(request):
    uemail = request.POST.get("email")
    umessage = request.POST.get("message")
    inserdata = complete_fitting(email=uemail,message=umessage)
    inserdata.save()
    return render(request,'service-details-2.html')

def hello(request):
    usersname = request.POST.get("username")
    usersemail = request.POST.get("email")
    usersphone = request.POST.get("phone")
    userssubject = request.POST.get("subject")
    usersmessage = request.POST.get("message")
    savealldata = contact_us(name=usersname,email=usersemail,phone=usersphone,subject=userssubject,message=usersmessage)
    savealldata.save()
    return render(request,'contact.html')

def newimage(request):
    servic = Service.objects.all()
    context = {'newdata': servic}
    return render(request, 'index.html', context)

def secondgalleryimg(request):
    second = gimage.objects.all()
    context = {'data' : second}
    return render(request,'gallery.html',context)

def category(request):
    new_data = productCategory.objects.all()
    context = {'first_data' : new_data}
    return render(request,'category.html',context)


def products(request):
    if request.method == "POST":
        cateid = request.POST.get("cateid")
        productdata = product.objects.filter(category=productCategory(id=cateid))
        context = {'productdata' : productdata}
        return render(request,'products.html', context)
    return render(request, "products.html")

def scategory(request):
    product_data = Pcategory.objects.all()
    context = {'firstproduct': product_data}
    return render(request,'shopcategory.html', context)

def shop_details(request):
    if request.method == "POST":
        catid = request.POST.get("cateid")
        pdata = sdetials.objects.filter(category_id=catid)
        context = {'seconddata': pdata}
        return render(request, 'shop-details.html', context)
    return render(request, 'shop-details.html')

def login(request):
    return render(request,'login.html')

def shop(request):
    return render(request,'shop.html')