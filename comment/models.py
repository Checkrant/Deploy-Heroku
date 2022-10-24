from django.db import models

# Create your models here.
class Comment(models.Model):
    data =  models.DateTimeField(max_length=256)
    content = models.TextField(max_length=350)
    
    def __str__(self) -> str:
        return self.content