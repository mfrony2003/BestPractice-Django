from django.db import models

class Answer(models.Model):
    id=models.AutoField(primary_key=True)
    answer = models.CharField(max_length=100)
    image=models.ImageField(upload_to='answer/')    
    def __str__(self):
        return self.answer