from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.
class timedelivery(models.Model):
  email = models.EmailField(verbose_name="user email")
  message = models.TextField(verbose_name="user message")

class complete_fitting(models.Model):
  email = models.EmailField(verbose_name="user email")
  message = models.TextField(verbose_name="user message")

class contact_us(models.Model):
  name = models.CharField(max_length=100)
  email = models.EmailField()
  phone = models.BigIntegerField()
  subject = models.CharField(max_length=100)
  message = models.TextField()


class Service(models.Model):
  title = models.CharField(max_length=50)
  description = models.TextField()
  interiorphoto = models.ImageField(upload_to='photos')
  def photo(self):
    return mark_safe('<img src ="{}" width = "100"/>'.format(self.interiorphoto.url))
  photo.allow_tags =True

class gimage(models.Model):
  title = models.CharField(max_length=30 , verbose_name='title')
  image = models.ImageField(upload_to='photos' , verbose_name ='gallery image')
  def gphoto(self):
    return mark_safe('<img src ="{}" width = "100"/>'.format(self.image.url))
  gphoto.allow_tags = True

class blogimage(models.Model):
  bimage = models.ImageField(upload_to='photos' , verbose_name='blog image')
  title = models.CharField(max_length=30 , verbose_name='blog title')
  description = models.TextField(verbose_name='Description')

  def bphoto(self):
    return mark_safe('<img src = "{}" width = "100"/>'.format(self.bimage.url))
  bphoto.allow_tags = True

class productCategory(models.Model):
  name = models.CharField(max_length=60)
  image = models.ImageField(upload_to="category")

  def __str__(self):
    return self.name

  def categoryphoto(self):
    return mark_safe('<img src = "{}" width = "100"/>'.format(self.image.url))


class product(models.Model):
  category = models.ForeignKey(productCategory, on_delete=models.CASCADE)
  name = models.CharField(max_length=60)
  materialType = models.CharField(max_length=60)
  color = models.CharField(max_length=50)
  price = models.FloatField()
  description = models.TextField()
  qty = models.IntegerField()
  image = models.ImageField()
  status = models.BooleanField(default=1)

  def productphoto(self):
    return mark_safe('<img src = "{}" width = "100"/>'.format(self.image.url))

class Pcategory(models.Model):
  name = models.CharField(max_length=30)
  image = models.ImageField(upload_to='photos')

  def __str__(self):
    return self.name

  def pphoto(self):
    return mark_safe('<img src = "{}" width = "100"/>'.format(self.image.url))

class sdetials(models.Model):
  category = models.ForeignKey(Pcategory,on_delete=models.CASCADE)
  name = models.CharField(max_length=60)
  materialType = models.CharField(max_length=60)
  color = models.CharField(max_length=50)
  description = models.TextField(max_length=40)
  price = models.FloatField()
  value = models.CharField(max_length=30)
  qty = models.IntegerField()
  image = models.ImageField()
  status = models.BooleanField(default=1)

  def productimage(self):
    return mark_safe('<img src = "{}" width = "100"/>'.format(self.image.url))