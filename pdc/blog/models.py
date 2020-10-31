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
    doctors_prescription=models.CharField(max_length=10, default="yes")
    days=models.CharField(max_length=10, default="14")
    test=models.CharField(max_length=10, default="yes")
    covid=models.CharField(max_length=10, default="yes")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
    