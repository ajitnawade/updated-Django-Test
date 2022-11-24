from django.db import models
from django.utils import timezone
from django.contrib import auth
# from django import models
# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=30)
    job = models.CharField(max_length=30)
    username = models.CharField(max_length=20)
    userpass = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name


class Client(models.Model):
    client_name = models.CharField(max_length=30)
    createdat = models.DateTimeField(default=timezone.now())
    updateat = models.DateTimeField(blank=True,null=True)
    createdby = models.CharField(max_length=40,default="admin")

    def update(self):
        self.updateat = timezone.now()
        self.save()
    def __str__(self):
        return self.client_name


class Project(models.Model):
    project_name = models.CharField(max_length=30)
    client = models.ForeignKey(Client,on_delete=models.CASCADE)
    users = models.ManyToManyField(Users)
    createdat = models.DateTimeField(default=timezone.now())
    updateat = models.DateTimeField(blank=True,null=True)
    createdby = models.CharField(max_length=40)
    def __str__(self):
        return self.project_name
    
    def update(self):
        self.updateat = timezone.now()
        self.save()

    def users_info(self):
        return ','.join([str(p) for p in self.users.all()])
    

