from django.db import models
from django.utils import timezone
from django.conf import settings
from django.core.validators import RegexValidator

# Create your models here.
class Supplement(models.Model):
    name = models.CharField(max_length=200,unique=True, blank=False, null=False)
    supplementType = models.CharField(max_length=50, blank=False, null=False)
    image = models.ImageField(upload_to='supplements')
    details = models.CharField(max_length=300)
    createdOn = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Message(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=False, null=False) # validators should be a list
    email = models.EmailField(max_length = 254, blank=False, null=False)
    message = models.TextField(blank=False, null=False)
    createdOn = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name