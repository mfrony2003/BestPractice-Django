from django.db import models

class Question(models.Model):
    id=models.AutoField(primary_key=True)
    question = models.CharField(max_length=100)
    image=models.ImageField(upload_to='question/')    
    def __str__(self):
        return self.question