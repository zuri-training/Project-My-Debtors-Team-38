from django.db import models
from datetime import datetime
from accounts.models import Guardian, School, Student


# Create your models here.

class Post(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(datetime.now)
    updated_at = models.DateTimeField(datetime.now)


class Contend(models.Model):
    guardian = models.ForeignKey(Guardian, on_delete=models.CASCADE)
    post = models.OneToOneField(Post, on_delete=models.CASCADE)
    made_payment = models.BooleanField(default=False)
    reason = models.CharField(max_length=50)
    receipt = models.FileField(upload_to="")
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(datetime.now)


class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body[:20]
