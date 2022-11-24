from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth import authenticate
from .forms import LoginAdmin,ClientForm,LoginUser
from django.http import HttpResponse
from django.contrib import auth
from .models import Client,Project,Users

# Create your views here.

def interface(request):
    return render(request,'app1/interface.html')

def adminlogin(request):
    if request.method == "POST":
        loginform = LoginAdmin(request.POST)
        if loginform.is_valid():
            us =  request.POST["email"]
            ps =  request.POST["password"]
            user=  authenticate(username=us,password =ps)
            if user is not None:
                form=ClientForm()
                clts = Client.objects.all()
                return render(request,'app1/yes.html',{'form':form,'clts':clts})
            else:
                return render(request,'app1/no.html')

    else:
        loginform = LoginAdmin()      

    return render(request,'app1/adminlogin.html',{'form':loginform})


def userlogin(request):
    form = LoginUser()
    if request.method == 'POST':
            us =  request.POST["username"]
            ps =  request.POST["password"]
            try:
                data = Users.objects.get(username=us,userpass = ps)
                name = data.name
                # user = Users.objects.get()
                proj = Project.objects.all()
                l1={}
                for i in proj:
                    if name in i.users_info():
                        l1[i.id]=i.project_name
                return render(request,'app1/userhome.html',{'user_name':name,'proj':l1})
            except:
                return render(request,'app1/no.html')
    return render(request,'app1/userlogin.html',{'form':form})


def cltupdate(request,id):
    data=Client.objects.get(pk=id)
    form = ClientForm(instance=data)
    if request.method=='POST':
        form = ClientForm(request.POST,instance=data)
        if form.is_valid(): 
            data.update()
            form.save()
            
            form=ClientForm()
    else:
        form = ClientForm(instance=data)
    return render(request,'app1/updateclt.html',{'form':form})


def cltdelete(request,id):
    clt=Client.objects.get(pk=id)
    clt.delete()
    return render(request,'app1/delete.html')

def cltview(request,id):
    clt=Client.objects.get(pk=id)
    proj=Project.objects.filter(client=id)
    return render(request,'app1/viewclt.html',{'clt':clt,'proj':proj})

def addclt(request):
    form=ClientForm()
    if request.method == "POST":
        clt = ClientForm(request.POST)
        if clt.is_valid():
            clt.save()   
            clt = ClientForm()
    else:
        clt =  ClientForm()  
    clts = Client.objects.all()
    return render(request,'app1/yes.html',{'form':form,'clts':clts})

def proj_detail(request,id):
    dtl=Project.objects.get(pk=id)
    return render(request,'app1/project_details.html',{'dtl':dtl})