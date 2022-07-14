from django.db import models
from book.mixins import TranslateMixin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
import os
from datetime import datetime
import random


def upload_to(name):
    def handle(instance, filename):
        ext = os.path.splitext(filename)[1]


        return "{}/{:%Y}/{:%m}/{:%Y.:%m.:%H:%M.:%S}-{}{}".format(
            name,
            datetime.now(),
            datetime.now(),
            datetime.now(),
            random.randint(1, 999999),
            ext
        )
    return handle

def post_upload_to(instance, filename):
    return upload_to('posts')(instance, filename)


def carousel_upload_to(instance, filename):
    return upload_to('carousel')(instance, filename)


class Carousel(models.Model):
    ACTIVE = 1
    INACTIVE = 0
    image = models.ImageField(upload_to=carousel_upload_to)
    header = models.CharField(max_length=50, default=None, null=True)
    comment = models.CharField(max_length=150, default=None, null=True)
    status = models.SmallIntegerField(default=INACTIVE, choices=(
        (ACTIVE, 'Faol'),
        (INACTIVE, 'Nofaol')
    ))






class Category(TranslateMixin, models.Model):
    translate_attributes = ["name"]
    name_uz = models.CharField(max_length=60)
    name_en = models.CharField(max_length=60)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'



class Post(TranslateMixin, models.Model):
    translate_attributes = ["subject", "content"]

    user = models.ForeignKey(User, models.RESTRICT, default=None, null=True)
    category = models.ForeignKey(Category, models.RESTRICT, default=None, null=True)
    subject_uz = models.CharField(max_length=100, verbose_name=_("Sarlavha (uz)"))
    subject_en = models.CharField(max_length=100, verbose_name=_("Sarlavha (en)"))
    content_uz = models.TextField(verbose_name=_("Izoh (uz)"))
    content_en = models.TextField(verbose_name=_("Izoh (en)"))
    image = models.ImageField(default=None, null=True, blank=True, verbose_name=_("Rasm"), upload_to= post_upload_to)
    read = models.IntegerField(default=0)
    added_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
