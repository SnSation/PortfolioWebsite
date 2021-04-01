from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    path = models.CharField(max_length=500)
    category = models.CharField(max_length=500)

    def __str__(self):
        return self.name