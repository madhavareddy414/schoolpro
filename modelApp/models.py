from django.db import models
class Students(models.Model):
    eno = models.IntegerField()
    ename= models.CharField(max_length=30)
    esal = models.FloatField()
    eaddr = models.CharField(max_length=30)

