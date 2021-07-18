from django.db import models



# Create your models here.
class StudentRegister(models.Model):
    gender_val = [('male','male'),('female','female')]
    name = models.CharField(max_length=100)
    email=models.EmailField(max_length=40,null=True)
    phone = models.CharField(max_length=10)
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=10, choices=gender_val)
    dob = models.DateField(null=True)

    def ___str___(self):
        return self.name

class FacultyRegister(models.Model):
    gender_val = [('male','Male'),('female','Female')]
    name = models.CharField(max_length=100)
    email=models.EmailField(max_length=40,null=True)
    phone = models.CharField(max_length=10)
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=10, choices=gender_val)
    dob = models.DateField(null=True)

    def ___str___(self):
        return self.name