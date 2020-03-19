from django.db import models

# Create your models here.
class French(models.Model):
    branch_name = models.CharField(max_length=30)
    owener_name = models.CharField(max_length=30)
    city = models.CharField(max_length=20)
    image = models.ImageField(upload_to="image/")
    cover_pic = models.ImageField(upload_to="image/")
    email = models.CharField(max_length=50)
    contact = models.CharField(max_length=12)
    address = models.TextField(max_length=100)
    discription = models.TextField(max_length=300)
    Register_date = models.DateField()

    def __str__(self):
        return self.branch_name