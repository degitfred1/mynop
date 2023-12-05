from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import buy
from .forms import mybuy




def wap(request):
    return render(request,'index.html1')

def load1(request):
    return render(request,'index.1')    
    
   
def load2(request):
    return render(request,'index.2')
    

def load3(request):
    return render(request,'index.3')

def load4(request):
    return render(request,'index.4')
  
   
def load5(request):
    return render(request,'index.5')
    
    
    

def load6(request):
    return render(request,'index.6')


def load7(request):
    return render(request,'index.7')
    
    
    
    
def load8(request):
    return render(request,'index.8')
    
    
    
def get(request):
    van=buy.objects.all() 
    return render(request,'index.9',{"van":van})
    
    
def create(request):
    if request.method=="POST":
       form=mybuy(request.POST)
       if form.is_valid():
          form.save()
          return HttpResponse("purchase successfull")
          return redirect("/wap")
          
    else:
       form=mybuy()
       return render(request,'index.10',{"form":form})
       
       
       
def home(request):
    return render(request,'home.html')
    

          
          
             
def contact(request):
    return render(request,'contact.html')
     
          
           
       
def product(request):
    return render(request,'product.html')
         
         
               
       
def complain(request):
    return render(request,'complain.html')
    
        
         