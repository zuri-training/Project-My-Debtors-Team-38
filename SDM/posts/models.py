from django.db import models
from datetime import datetime

# Create your models here.


class Contend(models.Model):
    id = models.IntegerField(primary_key=True)
    debt_id = models.IntegerField()
    guardian_id = models.IntegerField()
    made_payment = models.BooleanField(default=False)
    receipt = models.ImageField()
    created_at = models.DateTimeField(default=datetime.now)



class Comments(models.Model):
    debt_id = models.IntegerField()
    school_id = models.IntegerField()
    id = models.IntegerField(primary_key=True)
    body = models.TextField()
    created_at = models.DateTimeField(datetime.now)
    updated_at = models.DateTimeField(datetime.now)

    def __str__(self):
        return self.body[:20]
    

