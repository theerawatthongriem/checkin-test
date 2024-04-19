from django.db import models
from django.contrib.auth.models import User

class Events(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=1000)
    time_start = models.DateTimeField()
    time_end = models.DateTimeField()
    detail = models.TextField()
    quantity_people = models.IntegerField()
    poster = models.FileField(upload_to='poster/')