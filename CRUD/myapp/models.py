from django.db import models

class Datas(models.Model):
    Name=models.CharField(max_length=20,default="")
    Age=models.IntegerField(max_length=20,default="")
    Address=models.CharField(max_length=50,default="")
    Contact=models.IntegerField(default="")
    Mail=models.CharField(max_length=50,default="")
