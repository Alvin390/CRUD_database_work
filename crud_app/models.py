from django.db import models

# Create your models here.
class Crud(models.Model):
    photo=models.ImageField(upload_to='upload',default='a.png')
    name=models.CharField(max_length=60)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=30)
    phone_number=models.CharField(max_length=10)
    date_of_birth=models.DateField()
    def __str__(self):
        return self.name
