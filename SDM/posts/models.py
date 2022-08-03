from django.db import models
from datetime import datetime
from accounts.models import Guardian,School,Student


# Create your models here.

class Debt(models.Model):
    school_id = models.ForeignKey(School,on_delete=models.CASCADE)
    student_id = models.ForeignKey(Student,on_delete=models.CASCADE)
    debt_incured = models.IntegerField()
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(datetime.now)
    updated_at = models.DateTimeField(datetime.now)



class Contend(models.Model):
    debt_id = models.ForeignKey(Debt, on_delete=models.CASCADE)
    guardian_id = models.ForeignKey(Guardian, on_delete=models.CASCADE) 
    made_payment = models.BooleanField(default=False)
    receipt = models.ImageField() #think we should use charfield for links in production shar
    created_at = models.DateTimeField(default=datetime.now)


class Comments(models.Model):
    debt_id = models.ForeignKey(Debt, on_delete=models.CASCADE)
    school_id = models.ForeignKey(School,on_delete=models.CASCADE) 
    body = models.TextField()
    created_at = models.DateTimeField(datetime.now)
    updated_at = models.DateTimeField(datetime.now)

    def __str__(self):
        return self.body[:20]
    

