from django.db import models

# Create your models here.

class Car(models.Model):
    name = models.CharField('Car name', max_length=40)
    about = models.TextField('Car about')
    img = models.ImageField('Car image', upload_to='media')

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'


class About(models.Model):
    about = models.TextField('About text')

    def __str__(self):
        return self.about


class Footer(models.Model):
    phone = models.CharField('Phone', max_length=40)
    email = models.CharField('Email', max_length=40)
    adres= models.CharField('adres', max_length=40)
        
    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Footer'
        verbose_name_plural = 'Footers'
