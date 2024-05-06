from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home-page'),
    path('filter/<str:flag>',views.filter,name='filter'),
    path('register/', views.register, name='register'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.LogoutView, name='logout'),
    path('delete-task/<str:id>/', views.DeleteTask, name='delete'),
    path('mark-complete/<str:id>/', views.Update, name='mark'),
]