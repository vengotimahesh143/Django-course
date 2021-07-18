from django import forms



class StudentRegisterForm(forms.Form):
	gender_val = [('male','Male'),('female','Female')]
	name = forms.CharField(max_length=100)
	email=forms.EmailField()
	phone = forms.CharField(max_length=10)
	age = forms.IntegerField(required=False)
	gender = forms.ChoiceField(choices=gender_val)
	dob = forms.DateField(required=False)