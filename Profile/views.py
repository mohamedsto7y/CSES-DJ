from django.shortcuts import redirect, render
from .forms import *
from django.contrib import messages
# Create your views here.
def complete_profile(request):
    if request.method=="POST":
        form=ProfileCreation(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'تم استكمال البروفايل الخاص بك')
            return redirect('portifolio:profile')
    else:
        form=ProfileCreation()
    return render(request,'profile/complete_profile.html',{'form':form})
def update_profile(request):
    pass