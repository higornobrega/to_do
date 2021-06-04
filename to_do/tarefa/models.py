from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class TarefaBd(models.Model):
    contents = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)    

    def __str__(self):
        return str(self.id)
