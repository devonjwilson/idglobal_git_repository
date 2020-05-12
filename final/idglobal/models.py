from django.db import models

# Create your models here.
class Mailing_List(models.Model):
    email = models.EmailField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email