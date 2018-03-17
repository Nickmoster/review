from django.db import models
from grades.models import Grade
# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)
    gender = models.BooleanField()
    age = models.PositiveIntegerField()
    info = models.CharField(max_length=200)
    #定义关联关系
    grade = models.ForeignKey(Grade)
    def __str__(self):
        return self.name