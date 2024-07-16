from django.db import models


class Links(models.Model):
    date_time = models.CharField(max_length=50, null=False, blank=False)
    link = models.CharField(max_length=10000, null=False, blank=False)
