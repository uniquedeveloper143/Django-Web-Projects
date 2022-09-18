from django.db import models


class ProfileImage(models.Model):
    image = models.ImageField(upload_to='media/profile_img/')



