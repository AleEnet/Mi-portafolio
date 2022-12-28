from django.db import models


class Publication(models.Model):
    name = models.CharField(max_length= 50, null=False, blank=False)
    type = models.CharField(max_length= 50, null=True, blank=True)
    image = models.ImageField(null= True, blank= True)
    description = models.TextField()
    link = models.CharField(max_length= 50, null=True, blank=True)
    
    def __str__(self):
        return f"{self.name} - {self.type}"

# Create your models here.
