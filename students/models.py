from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import smart_text


class UserDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=40,null=True, blank=True)
    # Mr_VSIT = models.ForeignKey(
    #     User,
    #     null           = True,
    #     related_name   = 'mrvsit',
    #     blank          = True,
    #     on_delete = models.CASCADE
    #     )
    # Ms_VSIT = models.ForeignKey(
    #     User,
    #     null           = True,
    #     related_name   = 'msvsit',
    #     blank          = True,
    #     on_delete = models.CASCADE
    #     )

    Mr_VSIT = models.CharField(max_length=40,null=True, blank=True)
    Ms_VSIT = models.CharField(max_length=40,null=True, blank=True)
    voted = models.BooleanField(default=False)

    def __str__(self):
        return smart_text(self.user)
