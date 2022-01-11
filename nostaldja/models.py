from django.db import models

# Create your models here.
class Decade(models.Model):
    start_year = models.CharField(max_length = 50)


    def __str__(self):
        return self.start_year

class Fad(models.Model):
    name = models.CharField(max_length = 100)
    image_url = models.TextField()
    description = models.TextField()
    decade = models.TextField()

    def __str__(self):
        return self.name