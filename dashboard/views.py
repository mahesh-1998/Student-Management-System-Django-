from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404
from .models import Student
from .forms import Student_Register_Form
from Home import views

# Create your views here.

	
student_info = [{
  "prn": 16110028,
  "first_name": "mahesh",
  "last_name": "kamble",
  "mobile_no": "9762501815",
  "aadhar_no": "1234",
  "gender": "male",
  "dob": "19-10-1998",
  "email_id": "maheshvkamble674@gmail.com",
  "roll_no": 6028,
  "state": "MH",
  "local_address": "aaa",
  "course": "Engg",
  "branch": "CS",
  "class": "BE",
  "division": "A",
  "adm_cat": "CAP"
},
{
  "prn": 16110021,
  "first_name": "pranav",
  "last_name": "zagade",
  "mobile_no": "8668716185",
  "aadhar_no": "1234",
  "gender": "male",
  "dob": "11-01-1998",
  "email_id": "pranavzagade@gmail.com",
  "roll_no": 6028,
  "state": "MH",
  "local_address": "aaa",
  "course": "Engg",
  "branch": "CS",
  "class": "BE",
  "division": "A",
  "adm_cat": "CAP"
}]



def Home(request):
    #return HttpResponse('<h1>Welcome To Student Reg Sys. DashBoard</h1>')
    template_name = "dashboard/student_list_view.html"
    context={
                  'students':Student.objects.all()
                } 
    return render(request,template_name,context)
    

def Student_detail_view(request,std_id):
    prn = std_id
    template_name = "dashboard/student_detail_view.html"
    try:
        student_obj = Student.objects.get(PRN=prn)
    except:
        raise Http404
    context={
                  'student':student_obj
                } 
    return render(request,template_name,context)

def Student_delete_view(request,std_id):
    prn = std_id
    template_name = "dashboard/student_list_view.html"
    try:
        student_obj = Student.objects.get(PRN=prn)
        student_obj.delete()
    except:
        raise Http404
    context={
                  'students':Student.objects.all()
                } 
    return render(request,template_name,context)

def Student_create_view(request):
    #print(request.POST)
    template_name = "dashboard/student_create_view.html"
    form = Student_Register_Form(request.POST or None)
    print(form.errors)
    if form.is_valid():
      print("start if student")
      print(form.cleaned_data)
      student.PRN= form.cleaned_data('PRN')
      student.first_name = form.cleaned_data('first_name')
      student.last_name = form.cleaned_data('last_name')
      student.mobile_no = form.cleaned_data('mobile_no')
      student.email = form.cleaned_data('email')
      student.gender = form.cleaned_data('gender')
      student.state = form.cleaned_data('state')
      student.course = form.cleaned_data('course')
      student.branch = form.cleaned_data('branch')
      student.div = form.cleaned_data('div')
      student.adm_cat= form.cleaned_data('adm_cat')
      student.dob = form.cleaned_data('dob')
      student.save()
      print("end if student")
    context={
                    'form':form
              }
    print("if not execute")
    return render(request,template_name,context)  


def About(reqeust):
    #return HttpResponse('<h1>About</h1>')
    template_name = "dashboard/about.html"
    return render(reqeust,template_name,{'title':'About'})


