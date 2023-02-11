from django.urls import path
from . import views
import secrets
app_name = 'jobapp'


urlpatterns = [ 
    path('', views.home, name='home'),
    path('job-list/', views.job_list, name='job-list'),
    path('job-detail/<int:pk>/', views.job_detail, name='job-detail'),
    path('contact/', views.contact, name='contact'),
    path('success/<str:access_code>/', views.success, name='success'),
    path('login/', views.login_request, name='login'),
    path('signup/<str:access_code>/', views.signup, name='signup'),
    path('logout/', views.logout_request, name='logout'),
    path('generate_link/', views.generate_link, name='generate_link'),
    path('application_list/', views.application_list, name='application_list'),
    path('paystack/', views.paystack, name='paystack'),
    path('resume/<int:pk>/', views.resume, name='resume'),
    path('about/', views.about, name='about'),
]