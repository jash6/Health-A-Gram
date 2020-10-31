from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    weight=models.CharField(max_length=100, default='light')
    pregnant=models.CharField(max_length=10, default="no")
    anemia=models.CharField(max_length=10, default="no")
    infectious_diseases=models.CharField(max_length=10, default="no")
    doctors_prescription=models.ImageField(default='default.jpg',upload_to='prescription_pics')
    days=models.CharField(max_length=10, default="14")
    test=models.CharField(max_length=10, default="yes")
    covid=models.CharField(max_length=10, default="yes")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
    

class Donation(models.Model):
    receiver = models.CharField(max_length = 100)
    donor = models.CharField(max_length = 100)
    Hospital = models.CharField(max_length = 100)
    City = models.CharField(max_length = 100,default='')
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.donor