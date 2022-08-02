from django.db import models
from datetime import datetime

# Create your models here.


class Contend(models.Model):
    id = models.IntegerField(primary_key=True)#not needed django does it by default
    debt_id = models.IntegerField() #foriegn key
    guardian_id = models.IntegerField() #foriegn key
    made_payment = models.BooleanField(default=False)
    receipt = models.ImageField() #think we should use charfield for links in production shar
    created_at = models.DateTimeField(default=datetime.now)



class Comments(models.Model):
    debt_id = models.IntegerField()#foriegn key
    school_id = models.IntegerField()#foriegn key
    id = models.IntegerField(primary_key=True)#not needed django does it by default
    body = models.TextField()
    created_at = models.DateTimeField(datetime.now)
    updated_at = models.DateTimeField(datetime.now)

    def __str__(self):
        return self.body[:20]
    

