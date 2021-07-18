from django.shortcuts import render
from django.http import HttpResponse
from .forms import StudentRegisterForm
from .models import StudentRegister




# Create your views here.
def student_register(request):
    form=StudentRegisterForm(request.POST)
    if request.method=='POST':
        if form.is_valid():
            student=StudentRegister(name=request.POST.get('name'),email=request.POST.get('email'),phone=request.POST.get('phone'),age=request.POST.get('age'),gender=request.POST.get('gender'),dob=request.POST.get('dob'))
            student.save()
            return HttpResponse("student registratio done!!")
    return render(request,'user/student_register.html',{'form':form})