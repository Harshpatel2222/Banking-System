from django.db import models

# Create your models here.

class NewCustomer(models.Model):
    name = models.CharField(max_length=25)
    number = models.IntegerField()
    email = models.EmailField(max_length=50)
    current_balance = models.IntegerField()

    def __str__(self):
        return self.name
