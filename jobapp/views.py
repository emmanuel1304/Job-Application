from django.shortcuts import render, redirect
from .forms import *
from .models import *
# Create your views here.
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from django.contrib.auth import login, authenticate, logout 
from django.http import HttpResponse
from .models import OneTimeLinkModel
import random
import string
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'jobapp/home.html')

def job_list(request):
    jobs = Jobs.objects.all()
    context = {'job':jobs}
    return render(request, 'jobapp/job-list.html', context)    

@login_required(login_url='/login/')
def job_detail(request, pk):
    job = Jobs.objects.get(id=pk)                 
    return render(request, 'jobapp/job-detail.html', context={'job':job})


def contact(request):
    return render(request, 'jobapp/contact.html')

def success(request, access_code=0):
    if (access_code == 0):
        return HttpResponse("Test link")

    elif OneTimeLinkModel.objects.filter(one_time_code=access_code).exists():

        #remove the line below if you do not want the link to self destruct after it has been used
        OneTimeLinkModel.objects.filter(one_time_code=access_code).delete()
        return render(request, 'jobapp/success.html')  

    elif not OneTimeLinkModel.objects.filter(one_time_code=access_code).exists():
        return HttpResponse("<h1>Bad Or Expired Link</h1>")
    else:
        return render(request, 'jobapp/success.html')    
    
def signup(request, access_code):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('jobapp:home')
    else:
        form = SignUpForm()
    if (access_code == 0):
        return HttpResponse("Test link")

    elif OneTimeLinkModel.objects.filter(one_time_code=access_code).exists():

        #remove the line below if you do not want the link to self destruct after it has been used
        OneTimeLinkModel.objects.filter(one_time_code=access_code).delete()
        return render(request, 'jobapp/signup.html')  

    elif not OneTimeLinkModel.objects.filter(one_time_code=access_code).exists():
        return HttpResponse("<h1>Bad Or Expired Link</h1>")
    else:
        return render(request, 'jobapp/signup.html')    
      


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            request.session['user'] = username
            return redirect('jobapp:home')
    else:
        form = AuthenticationForm()
    return render(request, 'jobapp/login.html', context={"form":form})


def logout_request(request):
    logout(request)
    return redirect("jobapp:login")   

#generates the string of the one time URL
def randomString(stringLength=20):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

#generates the link itself
def generate_link(request):
    the_string = randomString(stringLength=20)
    OneTimeLinkModel.objects.create(one_time_code=the_string)
    return HttpResponse('<h1>Click the link for signup form </h1><br><a href="/signup/{}">{}{}</a>'.format(the_string,request.build_absolute_uri(), the_string))

@login_required(login_url='/login/')
def application_list(request):
    jobs = Application.objects.filter(user=request.user)
    print(jobs)
    return render(request, 'jobapp/application_list.html', context = {'job': jobs})


def paystack(request):
    return render(request, 'jobapp/paystack.html') 


def resume(request, pk):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        resume = request.POST.get('resume')
        letter = request.POST.get('letter')
        job = Jobs.objects.get(id=pk)
        application = Application.objects.create(user=request.user, name=name, email=email,resume=resume, letter=letter, job=job)
        application.save()
        return redirect('jobapp:application_list')
    
    return render(request, 'jobapp/resume.html', context={'job':job})
          

def about(request):
    return render(request, 'jobapp/about.html')          