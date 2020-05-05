from django.db import models

class NaverSports(models.Model):
    rank = models.IntegerField()
    url = models.CharField(max_length=300)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title