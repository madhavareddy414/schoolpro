from django.db import models

class Stud(models.Model):
    sname = models.CharField(max_length=30)
    sclass = models.CharField(max_length=30)
    saddr = models.CharField(max_length=30)
    semail = models.EmailField(max_length=30)

