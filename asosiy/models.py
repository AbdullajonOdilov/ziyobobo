from django.db import models

# Create your models here.

class News(models.Model):
    rasm= models.FileField()
    sarlavha = models.CharField(max_length=150)
    sana = models.DateField()
    matn = models.TextField()
    korishlar_soni = models.PositiveSmallIntegerField(default=0)
    def __str__(self): return self.sarlavha

