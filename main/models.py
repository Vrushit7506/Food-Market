from django.db import models
from django.contrib.auth import get_user_model
from django.core import validators


# Create your models here.

User = get_user_model()

class foodMenu(models.Model):
    foodtype = (
        ("1", "Veg"),
        ("2", "Non-Veg"),
    )

    all_cuisine = (
        ("1", "Soup"),
        ("2", "Salad"),
        ("3", "Appetizers"),
        ("4", "Italian Mainfare"),
        ("5", "Mexican Mainfare"),
        ("6", "Pastas"),
        ("7", "Pizzas"),
        ("8", "Rice"),
        ("9", "Fondue"),
        ("10", "Desserts"),
    )
    
    cuisine = models.CharField(choices=all_cuisine, max_length=50, blank=True)
    name = models.CharField(max_length=50, blank=True)
    price = models.IntegerField(null=True)
    foodtype = models.CharField(choices=foodtype, max_length=10)
    newest = models.BooleanField(default=False)
    recommended = models.BooleanField(default=False)
    ratings = models.IntegerField(validators=[
                              validators.MinValueValidator(1), validators.MaxValueValidator(5)], null=True, default=4)

    def __str__(self):
      return self.get_cuisine_display() + " - " + self.name

    class Meta:
      verbose_name_plural = "Food Menu"

class barMenu(models.Model):
    all_drinktype = (
        ("1", "Beer"),
        ("2", "Cocktail"),
        ("3", "Gin"),
        ("4", "Red Wine"),
        ("5", "Sparkling Wine"),
        ("6", "Vodka"),
        ("7", "Whiskey"),
        ("8", "White Wine"),
    )
    drinktype = models.CharField(choices=all_drinktype, max_length=50, blank=True)
    name = models.CharField(max_length=50, blank=True)
    current_price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    old_price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    tot_qty = models.IntegerField(null=True)
    actual_price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    savings = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    low = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    high = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    className = models.CharField(max_length=50, blank=True)
    recommended_drink = models.BooleanField(default=False) 

    def __str__(self):
        return self.get_drinktype_display() + " - " + self.name

    class Meta:
        verbose_name_plural = "Bar Menu"


class ordered(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    dish_name = models.CharField(max_length=50, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    qty = models.IntegerField(null=True)
    cooked = models.BooleanField(default=False)

    def __str__(self):
      return self.dish_name

    class Meta:
      verbose_name_plural = "Ordered"


class Message(models.Model):

    sender = models.ForeignKey(User, related_name="sent_messages", on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name="received_messages", on_delete=models.CASCADE)
    message = models.TextField()
    className = models.CharField(max_length=50, blank=True)
    seen = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("date_created",)
