from django.db import models

"""
Create a table provider_provider(
name varchar(32)...
)
"""
class Provider(models.Model):
    name = models.CharField(max_length=32)
    url = models.CharField(max_length=128, blank=True)
    email = models.CharField(max_length=128, blank=True)
    phone = models.CharField(max_length=128, blank=True)

    def __str__(self):
        return str(self.id) + ' (' + self.name + ')'
