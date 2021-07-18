from django.shortcuts import render
from django.http import HttpResponse
from .forms import StudentRegisterForm,FacultyRegistrationForm
from .models import StudentRegister,FacultyRegister
from django.core.mail import EmailMessage
from course import settings



# Create your views here.
def student_register(request):
    form=StudentRegisterForm(request.POST)
    if request.method=='POST':
        if form.is_valid():
            student=StudentRegister(name=request.POST.get('name'),email=request.POST.get('email'),phone=request.POST.get('phone'),age=request.POST.get('age'),gender=request.POST.get('gender'),dob=request.POST.get('dob'))
            student.save()

            name=form.data['name']
            receiver=form.data['email']
            sub = 'course registration'
            body = 'hi '+name+' Your Course Registration has been done successfully!!'

            sender = settings.EMAIL_HOST_USER

            email_msgs = EmailMessage(sub,body,sender,[receiver])
            email_msgs.send()

            return HttpResponse("student registratio done!!")
    return render(request,'user/student_register.html',{'form':form})


def faculty_register(request):
    form=FacultyRegistrationForm(request.POST)
    if request.method=='POST':
        if form.is_valid():
            form.save()
            return HttpResponse("Done!!")
    return render(request,'user/faculty_register.html',{'form':form})