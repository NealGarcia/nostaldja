from django.db import models

# Create your models here.
class Decade(models.Model):
    start_year = models.DateField()

    def __str__(self):
        return self.start_year

class Fads(models.Model):
    name = models.CharField(max_length = 100)
    image_url = models.CharField(max_length = 150)
    description = models.TextField()
    decade = models.DateField()

    def __str__(self):
        return self.name