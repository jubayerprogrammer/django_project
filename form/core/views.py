from django.shortcuts import render,redirect
from core.models import Profile
from core.forms import profileForm

# Create your views here.

def home(request):
    candidate = Profile.objects.all()
    if request.method == "POST":
        form = profileForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            print(f"hi")
           
    else:
        form = profileForm()
        print("hi2")
        print(form.errors)
        
    return render(request,"core/home.html",{"form":form,"candidate": candidate})             

 

def candidate(request,pk):
    candidate = Profile.objects.get(pk=pk)
    print(pk)
    return render(request,"core/candidate_info.html",{"candidate": candidate})