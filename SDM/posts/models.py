from django.db import models
from datetime import datetime
from accounts.models import Guardian,School,Student


# Create your models here.

class Debt(models.Model):
    school = models.ForeignKey(School,on_delete=models.CASCADE)
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    debt_incured = models.DecimalField(max_digits=11, decimal_places=2)
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(datetime.now)
    updated_at = models.DateTimeField(datetime.now)



class Contend(models.Model):
    guardian = models.ForeignKey(Guardian, on_delete=models.CASCADE) 
    made_payment = models.BooleanField(default=False)
    receipt = models.FileField(upload_to= ""  ) 
    created_at = models.DateTimeField(default=datetime.now)


class Comments(models.Model):
    debt_post = models.ForeignKey(Debt, on_delete=models.CASCADE)
    school = models.ForeignKey(School,on_delete=models.CASCADE) 
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body[:20]
    

