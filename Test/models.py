from django.db import models
from django.utils import timezone
from rest_framework.fields import JSONField


# Create your models here.

class member(models.Model):
    name = models.CharField(max_length=30)
    tz = models.CharField(max_length=30)

    def __repr__(self):
        return self.name

    class Meta:
        db_table = 'member'


class activities(models.Model):
    user_id = models.ForeignKey(member, on_delete=models.CASCADE)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)

    def __repr__(self):
        return str(self.user_id)

    class Meta:
        db_table = 'activities'


