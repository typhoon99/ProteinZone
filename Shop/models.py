from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.
class Supplement(models.Model):
    name = models.CharField(max_length=200,unique=True, blank=False, null=False)
    supplementType = models.CharField(max_length=50, blank=False, null=False)
    image = models.ImageField(upload_to='Shop/static/images/supplements/')
    details = models.CharField(max_length=300)
    createdOn = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name