#-*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User, AbstractUser

class MyUser(AbstractUser):
    nbPoke = models.IntegerField(default=0)
    def __unicode__(self):
        return "{}: {}".format(self.name, self.activeness.rating if self.activeness else "no rating")