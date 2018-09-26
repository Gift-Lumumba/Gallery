from django.db import models

# Create your models here.
class Location(models.Model):
  name = models.CharField(max_length = 30)
  description = models.TextField()

  def __str__(self):
      return self.name

  def save_location(self):
    self.save()

class Category(models.Model):
  name = models.CharField(max_length = 30)
  description = models.TextField()

  def __str__(self):
      return self.name

  def save_category(self):
    self.save()

class Image(models.Model): 
  name = models.CharField(max_length = 30)
  image = models.ImageField(upload_to = 'images/')
  description = models.TextField()
  location = models.ForeignKey(Location)
  category = models.ForeignKey(Category)

  def __str__(self):
      return self.name
  def save_image(self):
    self.save()
  