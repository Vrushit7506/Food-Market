from django.db import models

# Create your models here.

class ChatDB(models.Model):
  user = models.CharField(max_length=200, blank=True)
  text = models.TextField(blank=True)
  className = models.CharField(max_length=200, blank=True)
  chatno = models.AutoField(primary_key=True)

  def __str__(self):
        return self.user + " - " + str(self.chatno)
