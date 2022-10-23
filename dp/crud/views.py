from django.shortcuts import render
from django.http import HttpResponse
from .models import emp_det

# Create your views here.
def index(request):
    if request.method=="POST":
        fn=request.POST.get('fn')
        mn=request.POST.get('mn')
        ln=request.POST.get('ln')
        gender=request.POST.get('gender')
        dob=request.POST.get('dob')
        mobile=request.POST.get('mobileno')
        alternateno=request.POST.get('alternateno')
        email=request.POST.get('email')
        marital=request.POST.get('marital')
        bg=request.POST.get('bg')
        emp=emp_det(fn=fn,mn=mn,ln=ln,gender=gender,dob=dob,mobile=mobile,alternateno=alternateno,email=email,marital=marital,bg=bg)
        emp.save()
    return render(request,'crud/index.html')

def view(request):
    allvalues=emp_det.objects.all()
    context={'emp':allvalues}
    return render(request,'crud/view.html',context)


def tables(request):
     allvalues=emp_det.objects.all()
     context={'emp':allvalues}
     return render(request,'crud/table.html',context)
    