from django.db import models
from django.utils import timezone


# Create your models here.
class url_data(models.Model):
    url = models.CharField(max_length=200)
    count = models.IntegerField(default=1)
    date_updated = models.DateTimeField(auto_now=False, null=True)
    date_added = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.url