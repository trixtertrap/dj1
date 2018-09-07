from django.db import models


# Create your models here

class Query(models.Model):
    name=models.CharField(max_length=200)
    email=models.TextField(null=True)
    query=models.TextField()
    answer=models.TextField(null=True)


class AdminLogin(models.Model):
    name=models.CharField(max_length=200)
    password=models.TextField()

class Contact(models.Model):
    name=models.CharField(max_length=200,null=True)
    email=models.TextField(null=True)
    phone=models.IntegerField(null=True)
    suggestion=models.TextField(null=True)
    answer=models.TextField(null=True)

class EmployeeLogin(models.Model):
    name=models.CharField(max_length=200)
    password=models.TextField()



