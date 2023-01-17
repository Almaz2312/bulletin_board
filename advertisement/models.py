from django.contrib.gis.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


def get_upload_path_ad_image(instance, filename):
    return "ad_images/{username}/{file}".format(username=instance.advertisement.username(), file=filename)


def get_upload_path_head_image(instance, filename):
    return "ad_images/{username}/{file}".format(username=instance.username(), file=filename)


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    name = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.category}'


class Advertisement(models.Model):
    title = models.CharField(max_length=255)
    sub_category = models.ForeignKey(Subcategory, on_delete=models.DO_NOTHING, blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    location = models.CharField(max_length=64)
    description = models.TextField()
    head_image = models.ImageField(upload_to=get_upload_path_head_image, blank=True, null=True)

    def username(self):
        return self.owner.username

    def __str__(self):
        return self.title


class AdvertisementImage(models.Model):
    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_upload_path_ad_image, blank=True, null=True)


class Complain(models.Model):
    customer = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    text = models.TextField()
    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE)