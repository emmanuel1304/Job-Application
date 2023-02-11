from django.db import models
from django.contrib.auth.models import User
# Create your models here.
import uuid

class Jobs(models.Model):
    company_image = models.ImageField(null=True)
    job_name = models.CharField(max_length=300, blank=False)
    job_description = models.TextField(max_length=5000, blank=False)
    published_date = models.DateTimeField(auto_now_add=True)
    job_vacancy = models.CharField(max_length=50, blank=False)
    job_nature = models.CharField(max_length=50)
    job_salary = models.CharField(max_length=50)
    job_salary2 = models.CharField(max_length=50)
    job_location = models.CharField(max_length=500, blank=True)
    company_detail = models.TextField(max_length=5000, blank=True)
    responsibility1 = models.CharField(max_length=200, blank=True)
    responsibility2 = models.CharField(max_length=200, blank=True)
    responsibility3 = models.CharField(max_length=200, blank=True)
    responsibility4 = models.CharField(max_length=200, blank=True)
    
    qualification1 = models.CharField(max_length=200, blank=True)
    qualification2 = models.CharField(max_length=200, blank=True)
    qualification3 = models.CharField(max_length=200, blank=True)
    qualification4 = models.CharField(max_length=200, blank=True)
    
    def __str__(self):
        return self.job_name

    def get_jobs_by_id(id):
        return Jobs.objects.filter(id=id)


class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Jobs, on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=200, blank=True)
    email = models.EmailField(null=True, blank=True)
    resume = models.FileField(upload_to='images', blank=True)
    letter = models.CharField(max_length=10000, blank=True)
    status  = models.BooleanField(default=False)


    def __str__(self):
        return self.user.username


class MyUUIDModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # other fields        

class OneTimeLinkModel(models.Model):
    one_time_code = models.CharField(max_length=20)
    expiry_time = models.DateTimeField(auto_now_add=True, blank=True)
    #You would need an expiry time for the time based method
