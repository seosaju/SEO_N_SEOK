from django.db import models
from django.utils import timezone


# Create your models here.
class Menu(models.Model):
    MENU_CHOICES = {
        ('Tropical Revolution', 'Tropical Revolution'),
        ('Coffee', 'Coffee'),
        ('Ice Flakes', 'Ice Flakes')
    }

    image = models.ImageField()
    category = models.CharField(max_length=50, choices=MENU_CHOICES)
    korean_name = models.CharField(max_length=50)
    english_name = models.CharField(max_length=50)
    summary = models.TextField()
    kcal = models.IntegerField()
    salt = models.IntegerField()
    protein = models.IntegerField()
    fat = models.IntegerField()

    def __str__(self):
        return self.korean_name


class Inquiry(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.message


class Event(models.Model):
    banner = models.ImageField()
    main_image = models.ImageField()
    name = models.CharField(max_length=100)
    start_event_date = models.DateField()
    end_event_date = models.DateField()

    def __str__(self):
        return self.name
