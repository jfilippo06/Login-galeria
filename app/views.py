from multiprocessing import context
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import Send
from .models import *
# Create your views here.

def index(request):
    data = Post.objects.all()
    context = {'data':data}
    return render(request,'app/index.html',context)

@login_required
def admin(request):
    if request.method == 'POST':
        form = Send(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin-galery')
    else:
        form = Send()
    context = {'form':form}
    return render(request,'app/admin.html',context)