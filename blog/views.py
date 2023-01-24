from django.shortcuts import redirect,render
from django.http import HttpResponse
from blog.models import Blog,Contact
from django.contrib.auth.models import User
from django.contrib import messages
import math
# Create your views here.
def home(request):
     return render(request,'index.html')

def blog(request):
     no_of_posts= 7
     page = request.GET.get('page')
     if page is None:
          page=1
     else:
          page= int(page)
     blogs=Blog.objects.all()
     length=len(blogs)
     blogs=blogs[(page-1)*no_of_posts:page*no_of_posts]
     if page>1:
         prev=page-1
     else:
         prev=None

     if page<math.ceil(length/no_of_posts):
         nxt=page+1
     else:
          nxt=None
     context={'blogs':blogs,'prev':prev,'nxt':nxt}
     return render(request,'bloghome.html',context)

def blogpost(request,slug):
    blog = Blog.objects.filter(slug=slug).first()
    context={'blog':blog}
    return render(request,'blogpost.html',context)

def contact(request):
     if request.method == 'POST' :
          name=request.POST.get("name")
          email=request.POST.get("email")
          phone=request.POST.get("phone")
          desc=request.POST.get("desc")
          instance= Contact(name=name,email=email,phone=phone,desc=desc)
          instance.save()
     return render(request,'contact.html')

def search(request):
     return render(request,'search.html')

