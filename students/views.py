from rest_framework import generics
from django.shortcuts import render
from rest_framework import mixins
from students.models import Stud


from students.forms import StudentForm, SForm
from .models import Stud



def studentslist(request):
    return render(request,'students/home.html')

def register(request):
    title = "Student Registration"
    form = StudentForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data['sname']
        cls =form.cleaned_data['sclass']
        addr = form.cleaned_data['saddr']
        email =form.cleaned_data['semail']
        mail= Stud.objects.filter(semail=email)
        if len(mail)>0:
            return render(request,'students/ack.html',{'title':'Student Already Exists..Try with another E-mail'})
        else:
            p =Stud(sname=name,sclass=cls,saddr=addr,semail=email)
            p.save()
            return render(request,'students/ack.html',{'title':"Registered Scuccessfully"})


    context = {
        "title":title,
        "form":form
    }
    return render(request,'students/register.html',context)
def totalstudents(request):
    title= "All Students"
    queryset = Stud.objects.all()
    context ={
        "title":title,
        "queryset":queryset,

    }
    return render(request,"students/list.html",context)

def search(request):
    title="Search Student"
    form=SForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data['sname']
        queryset= Stud.objects.filter(sname=name)
        if len(queryset)==0:
            return render(request,'students/ack.html',{'title':'Student details not found Please enter correct data'})
        context ={
            'title':title,
            'queryset':queryset,

        }
        return render(request,'students/list.html',context)
    context = {
            "title":title,
            "form":form
    }
    return render(request,'students/search.html',context)


def delete(request):
    title="Delete Student"
    form=SForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data['sname']
        queryset = Stud.objects.filter(sname=name)
        if len(queryset)==0:
            return render(request,'students/ack.html',{'title':'Student details not found Please enter correct data'})
        else:
            queryset= Stud.objects.filter(sname=name).delete()

            return render(request,'students/ack.html',{"title":"Student Deleted Successfully"})
    context = {
            "title":title,
            "form":form
    }
    return render(request,'students/search.html')







