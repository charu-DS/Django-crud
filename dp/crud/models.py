from django.db import models

# Create your models here.
class emp_det(models.Model):
    # id=models.AutoField(primary_key=True)
    fn=models.CharField(max_length=100,null=True)
    mn=models.CharField(max_length=100,null=True)
    ln=models.CharField(max_length=100,null=True)
    gender=models.CharField(max_length=10,null=True)
    dob=models.CharField(max_length=20,null=True)
    mobile=models.CharField(max_length=20,null=True)
    alternateno=models.CharField(max_length=20,null=True)
    email=models.CharField(max_length=20,null=True)
    marital=models.CharField(max_length=20,null=True)
    bg=models.CharField(max_length=20,null=True)

