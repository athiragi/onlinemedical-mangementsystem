# from os import uname
from unicodedata import name
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Product,Contact,Order,Feedback
from .forms import OrderForm  

# from django.contrib import messages


# Create your views here.
def index(request):
    
    pro=Product.objects.all()
    return render(request,'index.html',{'medical':pro})
def logout(request):
    return render(request,"index.html")
def userlogin(request):
    if request.method == "POST":
        uname = request.POST.get("uname")
        pass1 = request.POST.get("pass1")
        myuser =  authenticate(username=uname,password =pass1)
        if myuser is not None:
            login(request,myuser)
            return redirect("/home")
        else:

            return redirect("/login")
            
    return render(request,"login.html")
def home(request):
    return render(request,"userhome.html")
def contact(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        phon=request.POST.get("num")
        desc=request.POST.get("desc")
        contact1=Contact(name=name,email=email,phoneno=phon,desc=desc)
        contact1.save()

  
    return render(request,"contact.html")


def Medicine(request):
    pro=Product.objects.all()
    return render(request,'medicine.html',{'medical':pro})
    # return render(request,"index.html")
    
    
def myorder(request):
   
    if not request.user.is_authenticated:
        return redirect("/login")
   # mymed=Medicines.objects.all()
    myprod=Product.objects.all()

    current_user=request.user.username
    # i am fetching the data from table MyOrders based on emailid
    items=Order.objects.filter(email=current_user)
    print(items)
    if request.method =="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        item=request.POST.get("items")
        quan=request.POST.get("quantity")
        address=request.POST.get("address")
        phon=request.POST.get("num")
        print(name,email,item,quan,address,phon)
        price=""
        for i in myprod:
            if item == i.name:
                price=i.price
            pass
        newprice=int(price)*int(quan)
        
        myuser=Order(name=name,email=email,items=item,address=address,quantity=quan,phoneno=phon,price=newprice)
        myuser.save()
        return redirect("/order")

    
    return render(request,"order.html",{'myprod':myprod})
def deleteOrder(request,id):
    print(id)
    user=Order.objects.get(id=id)
    user.delete()
    return redirect("/show")

def show(request):
   
    items=Order.objects.all()
 
    
    return render(request,"orderdetails.html",{'medical':items})  
def edit(request,id):
    items=Feedback.objects.get(id=id)
    return render(request,"edit.html",{'medical':items}) 
    
def update(request,id):
    items= Feedback.objects.get(id=id)
    # myprod=Product.objects.all()
    # medical={'item' :items}

    if request.method == "POST":
        items.name=request.POST.get("name")
        items.email=request.POST.get("email")
        items.phone=request.POST.get("num")
        items.feedback=request.POST.get("feedback")

        try:  
            items.save()
            return redirect('/feedbackshow')  
        except:  
            pass  
    return render(request,"edit.html",{'medical':items}) 
def feedback(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        phone=request.POST.get("num")
        feedback=request.POST.get("feedback")
        feed=Feedback(name=name,email=email,phone=phone,feedback=feedback)
        feed.save()
    return render(request,"feedback.html")
def feedbackdetail(request):
    items=Feedback.objects.all()
 
    
    return render(request,"feedbackdetail.html",{'medical':items})
def drop(request,id):
    medical= Feedback.objects.get(id=id)
    medical.delete()
    
    return redirect('/feedbackshow')  


    
def signup(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        email = request.POST.get("email")
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        pass1 = request.POST.get("pass1")
        cpass = request.POST.get("pass2")

        if(pass1 != cpass):
            return redirect("/signup")

        try:
            if User.objects.get(username=uname):
                return redirect("/signup")
        except:
            pass

        user= User.objects.create_user(uname, email, pass1)
        user.first_name = fname
        user.last_name = lname
        user.save()
        return redirect("/login")

    return render(request, "signup.html")

def about(request):
    return render(request,"about.html")
    
def search(request):
   
    # query=request.GET['query']
    # print(query)
    query=request.GET['query']
    allPostsMedicines=Product.objects.filter(name__icontains=query)
    # allPostsMedicines=Product.objects.all()

        
    para={"prod":allPostsMedicines}
    return render(request,"search.html",para)
    

