from django.urls import path,include,re_path
from . import views

urlpatterns = [
    path('', views.MyHome,name='home'),
    #path('login/',views.Login,name="home-login"),
    path('login/',views.Login,name="login"),
    path('student-signup/',views.Student_Signup,name='student-signup'),
    path('teacher-signup/',views.Teacher_Signup,name='teacher-signup'),
    path('parent-signup/',views.Parent_Signup,name='parent-signup'),
    path('student-signup/register/',views.Student_Register,name='student-register'),
    path('teacher-signup/register/',views.Teacher_Register,name='teacher-register'),
    path('parent-signup/register/',views.Parent_Register,name='parent-register'),
    path('login-delete/<int:std_id>/',views.Student_delete_view,name='student-delete'),
    path('login-year/',views.Student_list_view_year,name='student-year'),
    path('teacher-signup/register/<str:year>/',views.Teacher_Register,name='teacher-register'),
    path('login/attendance',views.Add_Attendance,name='attendance'),
    path('login/attendance1',views.Add_Attendance1,name='attendance1'),
    path('login/attendance2',views.Add_Attendance2,name='attendance2'),
    path('login/attendance3',views.Add_Attendance3,name='attendance3'),
    path('login/attendance4',views.Add_Attendance4,name='attendance4'),
    path('logout/', views.logout, name='logout'),
    path('login/parent',views.parent,name='parent'),
]
