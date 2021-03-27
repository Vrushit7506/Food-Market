from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class foodMenu(models.Model):
    foodtype = (
        ("1", "Veg"),
        ("2", "Non-Veg"),
    )
    cuisine = models.CharField(max_length=50, blank=True)
    name = models.CharField(max_length=50, blank=True)
    price = models.IntegerField(null=True)
    foodtype = models.CharField(choices=foodtype, max_length=10)

    def __str__(self):
      return self.cuisine + " - " + self.name

    class Meta:
      verbose_name_plural = "Food Menu"


class barMenu(models.Model):
    drinktype = models.CharField(max_length=50, blank=True)
    name = models.CharField(max_length=50, blank=True)
    price = models.IntegerField(null=True)
    uplimit = models.IntegerField(null=True)
    downlimit = models.IntegerField(null=True)
    totalorder = models.IntegerField(null=True)

    def __str__(self):
        return self.drinktype + " - " + self.name

    class Meta:
        verbose_name_plural = "Bar Menu"


class Message(models.Model):

    sender = models.ForeignKey(User, related_name="sent_messages", on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name="received_messages", on_delete=models.CASCADE)
    message = models.TextField()
    className = models.CharField(max_length=50, blank=True)
    seen = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("date_created",)
