from django.db import models

# Create your models here.
class Book(models.Model):
  judul = models.CharField(max_length=200)
  publish = models.DateTimeField("tanggal publikasi")

  def __str__(self):
    return str(self.judul)