from django.db import models
from Userprofile.models import UserModel

# Create your models here.


class Order(models.Model):

    CHOICES = {
        ('1', 'Pending'),
        ('2', 'Failed'),
        ('3', 'Successful'),
    }

    # user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    date = models.DateField()
    sender_name = models.CharField(max_length=225)
    sender_email = models.EmailField()
    sender_phone = models.CharField(max_length=225)
    sender_address = models.CharField(max_length=225)

    receiver_name = models.CharField(max_length=225)
    receiver_email = models.EmailField()
    receiver_phone = models.CharField(max_length=225)
    receiver_address = models.CharField(max_length=225)

    content = models.TextField()

    created = models.DateTimeField(auto_now=True)
