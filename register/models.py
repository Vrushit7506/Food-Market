from django.db import models

# Create your models here.

class User(models.Model):
  name = models.CharField(max_length=200,blank=True)
  phoneNum = models.IntegerField(null=True)
  tableNo = models.IntegerField(null=True)

  def __str__(self):
    return self.name + " - " + str(self.tableNo)