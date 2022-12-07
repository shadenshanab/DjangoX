from django.db import models
from django.urls import reverse
from accounts.models import CustomUser

# Create your models here.
# create new class

class Shop(models.Model):
    title = models.CharField(max_length=120)
    chef=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    description= models.TextField(blank=True, null=True)
    price= models.DecimalField(max_digits=5, decimal_places=2)
    picture= models.ImageField(default='https://cdn.discordapp.com/attachments/841047219549634580/1050055488366186598/bake-me-a-cake-high-resolution-logo-color-on-transparent-background.png')

    def str(self):
        return self.title

    def get_absolute_url(self):
        return reverse('shop-list')


