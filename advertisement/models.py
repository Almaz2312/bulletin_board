from django.db import models
from user.models import User


def get_upload_path_ad_image(instance, filename):
    return "ad_images/{username}/{file}".format(username=instance.advertisement.username(), file=filename)


def get_upload_path_head_image(instance, filename):
    return "ad_images/{username}/{file}".format(username=instance.username(), file=filename)


class Advertisement(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    head_image = models.ImageField(upload_to=get_upload_path_head_image, blank=True, null=True)

    def username(self):
        return self.user.username

    def __str__(self):
        return self.title


class AdvertisementImage(models.Model):
    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_upload_path_ad_image, blank=True, null=True)
