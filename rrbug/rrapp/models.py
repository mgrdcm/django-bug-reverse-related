from django.db import models

# Create your models here.


class Thing(models.Model):
    pass


class Category(models.Model):
    things = models.ManyToManyField(
        Thing,
        blank=True,
        related_name='categories',
    )
