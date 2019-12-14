from django.shortcuts import render, redirect
from dashboard.models import Student
from Home.models import Teacher,Subject,Attendance,Parent
from django.http import HttpResponse,Http404
import datetime
import time

# Create your views here.
def Login(request):
  
    student_template = "Home/student_login_view.html"
    teacher_template = "Home/teacher_login_view.html"
    parent_template = "Home/parent_login_view.html"
    error_template = "Home/base_error.html"
    

    if 'account_type' in request.session.keys():
      context = {}
      if request.session['account_type'] == 'student':
        email = request.session['student_id']
        student = Student.objects.filter(email=email).get()
        context['student'] = student
        return render(request,student_template,context)
      elif request.session['account_type'] == 'teacher':
        email = request.session['teacher_id']
        teacher = Teacher.objects.filter(email=email).get()
        context['teacher'] = teacher
        context['students'] = Student.objects.all()
        return render(request,teacher_template,context)
      elif request.session['account_type'] == 'parent':
        email = request.session['parent_id']
        p = Parent.objects.get(email=email)
        #parent = Parent.objects.filter(email=email).get()
        context['student'] = Student.objects.get(PRN=p.std_id)
        return render(request,parent_template,context)

    if request.method == 'POST':
      role = request.POST.get('role')
      email = request.POST.get('email')
      password = request.POST.get('password')
      print(role+email+password)
      if (role == "0" ):
          context={
            'message' : "Please Select Valid User Designation!..."
          }
          return render(request,error_template,context)
      elif (role == "1"):
          try:
            #print("role is student")
            s = Student.objects.get(email=email)
            print(s.first_name)
            if(s.password == password):
              print("user found pass matched")
              context={
                  'student':s
                }
              for key in list(request.session.keys()):
                del request.session[key]
              request.session['account_type'] = 'student'
              request.session['student_id'] = email
              return render(request,student_template,context)
            else:
              context={
                  'message' : "Password didn't match Please try again!..."
                } 
              return render(request,error_template,context)
          except:
            context={
            'message' : "Uers Doesnt Exists!..."
                    } 
            return render(request,error_template,context)
            #print("no user in db")
            #raise Http404
      elif (role == "2"):
          print("role is teacher")
          try:
            s = Teacher.objects.get(email=email)
            print(s.first_name)
            if(s.password == password):
              print("user found pass matched")
              context={
                  'students':Student.objects.all()
                }
              for key in list(request.session.keys()):
                del request.session[key]
              request.session['account_type'] = 'teacher'
              request.session['teacher_id'] = email
              return render(request,teacher_template,context)
            else:
              context={
                'message' : "Password didn't match Please try again!..."
              }
              return render(request,error_template,context)
              print("user found pass not matched")
          except Exception as e:
            print("i dont know")
            print(e)
            context={
            'message' : "Uers Doesnt Exists!..."
                    } 
            return render(request,error_template,context)
      elif (role == "3"):
          print("role is parent")
          try:
            p = Parent.objects.get(email=email)
            print(p.first_name)
            if(p.password == password):
              print("user found pass matched")
              context={
                  'student': p.std_id
                }
              for key in list(request.session.keys()):
                del request.session[key]
              request.session['account_type'] = 'parent'
              request.session['parent_id'] = email
              return render(request,parent_template,context)
            else:
              context={
                'message' : "Password didn't match Please try again!..."
              }
              return render(request,error_template,context)
              print("user found pass not matched")
          except Exception as e:
            print("i dont know")
            print(e)
            context={
            'message' : "Uers Doesnt Exists!..."
                    } 
            return render(request,error_template,context)
      else:
          print("role is admin")

    else:
      return redirect('/')

      if 'account_type' not in request.session.keys():
        return redirect('home')
        
def MyHome(request):
    return render(request,'Home/home.html')

def Student_Signup(request):
    return render(request,'Home/student_signup.html')

def Teacher_Signup(request):
    return render(request,'Home/teacher_signup.html')

def Parent_Signup(request):
    return render(request,'Home/parent_signup.html')

def Student_Register(request):
    if request.method == 'POST':
            #if request.POST.get('prn'):
                student=Student()
                student.PRN= request.POST.get('prn')
                student.first_name = request.POST.get('first_name')
                student.last_name = request.POST.get('last_name')
                student.mobile_no = request.POST.get('mobile_no')
                student.email = request.POST.get('email')
                student.gender = request.POST.get('gender')
                student.state = request.POST.get('state')
                student.course = request.POST.get('course')
                student.address = request.POST.get('address')
                student.branch = request.POST.get('branch')
                student.division = request.POST.get('div')
                student.adm_cat= request.POST.get('adm_cat')
                student.dob = request.POST.get('dob')
                student.password = request.POST.get('password')
                try:
                  student.save()
                except:
                  return HttpResponse("<h2 align=center>Student with Given PRN OR EMAIL already present...<h2>")
                #print("student")
                #print(student.division)
                #return HttpResponse("student")
                template_name = "Home/student_login_view.html"
                context={
                  'student':student
                } 
                return render(request,template_name,context)

    else:
      #print("in else")
      #return HttpResponse("else")
      template_name = "Home/login_register_error.html"
      return render(request,template_name)

def Teacher_Register(request):
    if request.method == 'POST':
            #if request.POST.get('prn'):
                teacher=Teacher()
                teacher.T_PRN= request.POST.get('tprn')
                teacher.first_name = request.POST.get('first_name')
                teacher.last_name = request.POST.get('last_name')
                teacher.mobile_no = request.POST.get('mobile_no')
                teacher.email = request.POST.get('email')
                teacher.gender = request.POST.get('gender')
                teacher.state = request.POST.get('state')
                teacher.course = request.POST.get('course')
                teacher.address = request.POST.get('address')
                teacher.department = request.POST.get('branch')
                print(teacher.T_PRN+teacher.first_name+teacher.last_name)
                print(teacher.mobile_no+teacher.email+teacher.gender+teacher.state+teacher.course)
                print(teacher.address+teacher.department)
                teacher.years = request.POST.getlist('years')
                print(teacher.years)
                teacher.subjects = request.POST.getlist('subjects')
                print(teacher.subjects)
                teacher.doj = request.POST.get('doj')
                teacher.password = request.POST.get('password')
                print(teacher.doj+teacher.password)
                try:
                  teacher.save()
                  print("teacher saved")
                except:
                  return HttpResponse("<h2 align=center>Student with Given TPRN OR EMAIL already present...<h2>")
                #print("student")
                #print(student.division)
                #return HttpResponse("student")
                template_name = "Home/teacher_login_view.html"
                context={
                  'students':Student.objects.all()
                } 
                return render(request,template_name,context)
    else:
      #print("in else")
      #return HttpResponse("teacher else")
      template_name = "Home/login_register_error.html"
      return render(request,template_name)


def Parent_Register(request):
    if request.method == 'POST':
            #if request.POST.get('prn'):
                parent=Parent()
                std_id = request.POST.get('std_id')
                parent.std_id = Student.objects.get(PRN=std_id)
                parent.first_name = request.POST.get('first_name')
                parent.last_name = request.POST.get('last_name')
                parent.mobile_no = request.POST.get('mobile_no')
                parent.email = request.POST.get('email')
                parent.gender = request.POST.get('gender')
                parent.password = request.POST.get('password')
                try:
                  parent.save()
                  print("parent saved")
                except:
                  return HttpResponse("<h2 align=center>Parent with Given Student_ID OR EMAIL already present...<h2>")
                template_name = "Home/parent_login_view.html"
                context={
                  'student':Student.objects.get(PRN=std_id)
                } 
                return render(request,template_name,context)
    else:
      #print("in else")
      #return HttpResponse("teacher else")
      template_name = "Home/login_register_error.html"
      return render(request,template_name)

def Student_delete_view(request,std_id):
    prn = std_id
    template_name = "Home/student_list_view.html"
    try:
        student_obj = Student.objects.get(PRN=prn)
        student_obj.delete()
    except:
        raise Http404
    context={
                  'students':Student.objects.all()
                } 
    return render(request,template_name,context)

def Student_list_view_year(request):
    template_name = "Home/student_list_view.html"    
    if request.method == "POST":
      year = request.POST['year']
      print(year)
      try:
          student_obj = Student.objects.all().filter(division=year)
      except Exception as e:
        print(e)    
      context={
                    'students':student_obj
                  } 
      return render(request,template_name,context)
    else:
      students = Student.objects.all()
      context={
                    'students':students
                  } 
      return render(request,template_name,context)

# def Add_Attendance(request):
#     template_name = "Home/attendance.html"
#     student_obj = Student.objects.all()
#     context={
#                   'students':student_obj
#                 } 
#     if request.method == "POST":
#       a = Attendance()
#       a.PRN = request.POST['prn']
#       a.subject_id = 100
#       a.status = request.POST['status']
#       a.date = request.POST['attend-date']
#       a.save()
#       print(a)
#       return render(request,template_name,context)

#     else:
#       print("in att")
#       return render(request,template_name,context)

def Add_Attendance(request):
    template_name = "Home/attendance.html"
    student_obj = Student.objects.all()
    context={
                  'students':student_obj
                } 
    if request.method == "POST":
      # a = Attendance()
      PRN = request.POST.getlist('prn[]')
      atten = request.POST.getlist('testName[]')
      dob=request.POST.getlist('dob[]')
      print(dob)
      print(atten)
     
      for i in range(0,len(PRN)):
        # print(temp)
        prn=PRN[i]
        a=atten[i]
        dobirth=dob[i]
        # print(prn)
        # print(x)
        y=request.POST['attend-date']
        print(y)
        
        a=Attendance(PRN=prn,subject_id=100,status=a,date=y,dob=dobirth)
        a.save()
        # a.PRN=temp
        # a.subject_id = 100
        # a.status = request.POST['status']
        # a.date = request.POST['attend-date']
        
      # print(a)
      return render(request,template_name,context)

    else:
      print("in att")
      return render(request,template_name,context)


def Add_Attendance1(request):
  template_name = "Home/attendance1.html"
  student= Student.objects.filter(division='FE')
  context1={
                  'students':student
                }
  return render(request,template_name,context1)

def Add_Attendance2(request):
  template_name = "Home/attendance1.html"
  student= Student.objects.filter(division='SE')
  context1={
                  'students':student
                }
  return render(request,template_name,context1)

def Add_Attendance3(request):
  template_name = "Home/attendance1.html"
  student= Student.objects.filter(division='TE')
  context1={
                  'students':student
                }
  return render(request,template_name,context1)

def Add_Attendance4(request):
  template_name = "Home/attendance1.html"
  student= Student.objects.filter(division='BE')
  context1={
                  'students':student
                }
  return render(request,template_name,context1)

def logout(request):

  for key in list(request.session.keys()):
        del request.session[key]

  return redirect('home')

def parent(request):
  
  if request.method == "POST":
    PRN1 = request.POST['prn']
    PRN2=int(PRN1)
    dob1 = request.POST['dob']
    dob2=dob1
    # print(PRN1)
    queryset=Student.objects.values_list('PRN',flat=True)
    queryset1=Student.objects.values_list('dob',flat=True)
    studdata=Student.objects.get(PRN=PRN2)
    mydate=time.strftime('%Y-%m-%d') 
    # print(livedate)
    attend=Attendance.objects.filter(PRN=PRN2,status='Yes',date=mydate)
    Attendace_count=len(attend)
    print(attend)
    

    for i in queryset:
        if (PRN2==i):
          print(PRN1)
          for j in queryset1:
            if (dob2==j):
              print(dob1)
              template_name = "Home/parentview.html"
              data={
                      "showdata":studdata,
                       "count":Attendace_count

              }
              return render(request,template_name,data)
              
        else:
          pass
    template_name = "Home/parent.html"  
    data={
                      "myname":"SRY!!! WRONG PRN OR DATE OF BIRTH",
                }
    return render(request,template_name,data)       
  

  else:
    template_name = "Home/parent.html"
    return render(request,template_name)
    print("in else")



