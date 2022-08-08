from django.db import models
from datetime import datetime
from accounts.models import School
from posts.models import Debt

# Create your models here.
class SchoolMessage(models.Model):
  school = models.ForeignKey(School, on_delete=models.CASCADE)
  receiver_id = models.IntegerField()
  debt = models.ForeignKey(Debt, on_delete=models.CASCADE)
  body = models.TextField()
  created_at = models.DateTimeField(default=datetime.now)

