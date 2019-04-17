from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import smart_text


class UserDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Mr_VSIT = models.CharField(max_length=40,null=True, blank=True)
    Ms_VSIT = models.CharField(max_length=40,null=True, blank=True)
    Popular = models.CharField(max_length=40,null=True, blank=True)
    vote4 = models.CharField(max_length=40,null=True, blank=True)
    voted = models.BooleanField(default=False)

    def __str__(self):
        return smart_text(self.user)
