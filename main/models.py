from django.db import models

# Create your models here.


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


class ChatDB(models.Model):
    user = models.CharField(max_length=200, blank=True)
    text = models.TextField(blank=True)
    className = models.CharField(max_length=200, blank=True)
    chatno = models.AutoField(primary_key=True)

    def __str__(self):
        return self.user + " - " + str(self.chatno)
