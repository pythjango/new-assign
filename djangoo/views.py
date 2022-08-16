from django.shortcuts import render
def djangoo_master(request):
    return render (request,'frame/master.html')

def djangoo_home(request):
    return render (request,'frame/home.html')

def djangoo_about(request):
    return render (request,'frame/about.html')

def djangoo_contact(request):
    return render (request,'frame/contact.html')

    

       

# Create your views here.
