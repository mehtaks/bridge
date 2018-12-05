from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class CompanyName(models.Model):
    company_name = models.TextField(max_length=50)


class UserComapny(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    company_id = models.ForeignKey(CompanyName,on_delete=models.CASCADE)

