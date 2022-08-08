
import datetime
from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    cars = models.ManyToManyField('Car', verbose_name="user's car")


STATUS_CHOICES = (
    ('R', 'Reviewed'),
    ('N', 'Not Reviewed'),
    ('E', 'Error'),
    ('A', 'Accepted')
)

class Website(models.Model):
    name = models.CharField(max_length=30)
    url = models.URLField()
    release_date = models.DateField()
    rating = models.IntegerField()
    status = models.CharField(choices=STATUS_CHOICES, max_length=1)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)   #si se borra el usuario, se borra el sitio web

    class Meta:
        ordering = ['rating']
        #db_table = 'website_custom_table_name'
        verbose_name = 'The Website'
        verbose_name_plural = 'The Websites'

    def was_released_last_week(self):
        if self.release_date < datetime.date(2022,7,6):
            return "Released before last week"
        else:
            return "Released this week"

    @property
    def get_full_name(self):
        return f"This is the complete name of the website: {self.name}"

    def __srt__(self):
        return self.name

    def get_absolute_url(self):
        return f"/websites/{self.id}"
    
    def save(self, *args, **kwargs):
        print("Estamos guardando")
        super().save(*args, **kwargs)



class Car(models.Model):
    name = models.CharField(max_length=40, primary_key=True)

