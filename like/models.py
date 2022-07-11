from django.db import models
from django.contrib.auth.models import User
from housing.models import House


class Like(models.Model):
    user_id = models.ForeignKey(User, related_name="liked_user")
    house_id = models.ForeignKey(House, related_name="liked_house")
    has_liked = models.BooleanField(default=True)

    def __str__(self):
        return "User " + self.user_id.username + " liked house " + self.house_id.name + str(self.has_liked)