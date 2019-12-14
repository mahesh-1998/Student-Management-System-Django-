from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home,name='student-list'),
    path('<int:std_id>/',views.Student_detail_view,name='student-detail'),
     path('create-new/',views.Student_create_view,name='create-student'),
     path('delete/<int:std_id>',views.Student_delete_view,name='delete-student'),
    path('about/',views.About,name='dash-about')
]
