# from urllib import request
from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentRegistration
from .models import User
# Create your views here.

# This function for Create and Read
def addshow(request):
    if request.method == 'POST':
        # breakpoint()
        fm = StudentRegistration(request.POST)
        user =  User.objects.filter(email=request.POST.get('email'))
        if not user:
            if fm.is_valid() and not user:
                nm = fm.cleaned_data['name']
                em = fm.cleaned_data['email']
                pw = fm.cleaned_data['password']
                obj = User(name=nm, email=em, password=pw)
                obj.save()
                fm = StudentRegistration()
            
        # fm.save()
    else:
        fm = StudentRegistration()
    stud = User.objects.all()
    return render(request, 'application/addshow.html',{'form':fm,'stu':stud})

# This function update the data
def update(request,id):
    if request.method == 'POST':
        user_obj = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=user_obj)
        if fm.is_valid():
            fm.save()
    else:
        user_obj = User.objects.get(pk=id)
        fm = StudentRegistration(instance=user_obj)
    return render(request, 'application/update.html',{'form':fm})

# This function for delete
def delete(request, id):
    if request.method == "POST":
        user_obj = User.objects.get(pk=id)
        user_obj.delete()
        return HttpResponseRedirect('/')