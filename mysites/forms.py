from django import forms

class Student_Register_Form(forms.Form):
    PRN = forms.IntegerField()
    first_name = forms.CharField()
    last_name= forms.CharField()
    mobile_no = forms.CharField()
    email = forms.EmailField()
    gender = forms.CharField()
    address = forms.CharField(forms.Textarea)
    state = forms.CharField()
    course = forms.CharField()
    branch = forms.CharField()
    division = forms.CharField()
    adm_cat = forms.CharField()
    dob = forms.DateField()