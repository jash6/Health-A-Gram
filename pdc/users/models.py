from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(default = 'default.jpg', upload_to='profile_pics')
    gender = models.CharField(max_length=10, default="")
    age = models.IntegerField(default=1)
    blood_group = models.CharField(max_length=50, default="")
    district = models.CharField(max_length=10, default="")
    # Hospital = models.ImageField(_(""), upload_to=None, height_field=None, width_field=None, max_length=None)
    Hospital = models.CharField(max_length=10, default="")
    has_corona = models.CharField(max_length=10, default="")
    is_donor = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} Profile'

class DonorDetails(models.Model):
    user = models.OneToOneField(Profile, on_delete = models.CASCADE)
    weight=models.IntegerField(default=1)
    pregnant=models.CharField(max_length=10, default="no")
    anemia=models.CharField(max_length=10, default="no")
    infectious_diseases=models.CharField(max_length=10, default="no")
    doctors_prescription=models.ImageField( upload_to='profile_pics')
    days=models.CharField(max_length=10, default="14")
    test=models.CharField(max_length=10, default="yes")
    covid=models.CharField(max_length=10, default="yes")

    def __str__(self):
        return f'{self.weight} Detail'
