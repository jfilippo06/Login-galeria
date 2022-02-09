from django.http import HttpRequest
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import Send
from .models import *
# Create your views here.

def index(request):
    return render(request,'app/index.html')

@login_required
def admin(request):
    if request.method == 'POST':
        form = Send(request.POST, request.FILES)
        if form.is_valid():
            HttpRequest(request,request.user)

            return redirect('admin-store')
    else:
        form = Send()
    context = {'form':form}
    return render(request,'app/admin.html',context)