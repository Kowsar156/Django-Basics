from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=50)
    cls = models.IntegerField()
    roll = models.IntegerField()
    class Meta:
        db_table = "student"