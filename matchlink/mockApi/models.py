from django.db import models
from django.utils import timezone

# Create your models here.

class ScmUser(models.Model):
    # user_type_id = models.BigIntegerField() #TODO
    username = models.CharField(max_length=128, null=True)
    password = models.CharField(max_length=64, null=True)
    firstname = models.CharField(max_length=64, null=True)
    lastname = models.CharField(max_length=128, null=True)
    # pincode = models.CharField(max_length=4, null=True)
    email = models.EmailField(null=False)
    mobile = models.CharField(max_length=16, null=True)
    birthday = models.DateField(null=True)
    # image_ref_id
    # enable_pin
    # enable
    # login_failed
    create_date = models.DateField(auto_now_add=True)
    create_by = models.CharField(max_length=128, blank=True)
    update_date = models.DateField(auto_now=True)
    update_by = models.CharField(max_length=128, blank=True)

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        # TODO create business card
        pass