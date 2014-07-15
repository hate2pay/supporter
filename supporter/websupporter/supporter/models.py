from django.db import models
from django.contrib.auth.models import User


class Ipaddress(models.Model):
    users = models.ManyToManyField(User)
    allowed_ip = models.IPAddressField(verbose_name="Allowed IP For Users")

    def __str__(self):
    	return self.allowed_ip

