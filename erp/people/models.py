from django.contrib.auth import get_user_model
from django.db import models

class UserInfo(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, primary_key=True)
    birthdate = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    tin = models.CharField(max_length=12, null=True, blank=True)
    sss = models.CharField(max_length=10, null=True, blank=True)
    philhealth = models.CharField(max_length=12, null=True, blank=True)
    pagibig = models.CharField(max_length=12, null=True, blank=True)
    # profile_pic = models.ImageField(null=True, blank=True, upload_to="")

    def __str__(self):
        return self.get_user_model().first_name