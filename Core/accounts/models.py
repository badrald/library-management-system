from django.db import models

from django.contrib.auth.models import User 

from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

def upload_pics(inctence,pic):
    return f"Profiles/{inctence.id}.{pic.split('.')[1]}"


class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    address= models.CharField(max_length=50, blank=True, null=True)
    phone_number=models.CharField(max_length=15,null=True,blank=True)
    user_photo=models.ImageField(upload_to=upload_pics,null=True,blank=True)
    borrowedBooks=models.IntegerField(default=0)
    boughtBooks=models.IntegerField(default=0)
    def __str__(self) :
        if self.user.first_name =='' or self.user.first_name == None:
            return self.user.username
        return self.user.first_name + " "+ self.user.last_name
    
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)