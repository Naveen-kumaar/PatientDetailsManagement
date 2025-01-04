from django.shortcuts import render,redirect
from xapp.models import patientdetails
from xapp.form import CustomUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def home(request):
    return render(request,"home.html")


def Register(request):
    form = CustomUserForm()
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registration Success you can Login Now ...")
            return redirect('/login')
    return render(request,'register.html',{"form":form})

def login_page(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method == 'POST':
            name = request.POST.get('username')
            pwd = request.POST.get('password')
            user = authenticate(request,username=name,password=pwd)
            if user is not None:
                login(request,user)
                messages.success(request,"Login successfully")
                return redirect("/")
            else:
                messages.error(request,"Invalid user name or password")
                return redirect("login/")

        return render (request,'login.html')

'''def Register(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        role = request.POST.get('role')
        password = request.POST.get('Password')
        C_Password = request.POST.get('C_Password')
        if password == C_Password:
            en = register(username=username,email=email,mobile=mobile,role=role,password=password,C_Password=C_Password)
            en.save()
            messages.success(request,'Your account has been successfully created...!')
            return redirect('login') 
        else:
            messages.warning(request,'password missmatching...!')
            return redirect('register')    
    return render(request,"register.html")

def login_page(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method == 'POST':
            name = request.POST.get('name')
            Password = request.POST.get('Password')
            print(name,Password)
            user = authenticate(request, username=name, password=Password)
            print(user)
            if user is not None:
                login(request,user)
                print(login(request,user))
                messages.success(request,"Login successfully...!")
                return redirect(request,'home')
            else:
                messages.error(request,"Login Failed")
                return redirect('login')
    return render(request,'login.html')'''

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.error(request,"Logout  successfully")
    return redirect ('home')


def create(request):
    if request.method == 'POST':
        date =request.POST.get('date')
        name =request.POST.get('name')
        age =request.POST.get('age')
        gender =request.POST.get('gender')
        address =request.POST.get('address')
        contactno =request.POST.get('contactno')
        history =request.POST.get('history')
        pain=request.POST.get('pain')
        duration=request.POST.get('duration')

        en =patientdetails(Date=date,Name=name,Age=age,Gender=gender,Address=address,Contactno=contactno,History=history,Pain=pain,Duration=duration)
        en.save()
        return redirect('view')
        
    return render(request,"create.html")

def view(request):
    mydata=patientdetails.objects.all()
    return render(request,'view.html',{'data':mydata})

def update(request,id):
    mydata = patientdetails.objects.get(id=id)
    if request.method =='POST':
        date =request.POST.get('date')
        name =request.POST.get('name')
        age =request.POST.get('age')
        gender =request.POST.get('gender')
        address =request.POST.get('address')
        contactno =request.POST.get('contactno')
        history =request.POST.get('history')
        pain=request.POST.get('pain')
        duration=request.POST.get('duration')

        mydata.Date=date
        mydata.Name=name
        mydata.Age=age
        mydata.Gender=gender
        mydata.Address=address
        mydata.Contactno=contactno
        mydata.History=history
        mydata.Pain=pain
        mydata.Duration=duration

        mydata.save()
        return redirect('/view')
    return render(request,'update.html',{'data':mydata})

def Delete(request,id):
    mydata = patientdetails.objects.get(id=id)
    mydata.delete()
    return redirect('/view')

def contact(request):
    
    return render(request,'contact.html')
