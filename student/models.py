import json

from django.db import models


# Create your models here.


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, default='')
    score = models.CharField(max_length=30, default='')
    email = models.CharField(max_length=30, default='')

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
