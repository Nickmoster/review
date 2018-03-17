from django.db import models

# Create your models here.
class Grade(models.Model):
    name = models.CharField(max_length=20)
    created_time = models.DateTimeField()
    girl_num = models.PositiveIntegerField()
    boy_num = models.PositiveIntegerField()
    description = models.CharField(max_length=256)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.name